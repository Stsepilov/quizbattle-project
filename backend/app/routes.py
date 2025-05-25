from flask import Blueprint, jsonify, request
from .models import Quiz, QuizItem, BattleRound, db
from sqlalchemy import func
import random

bp = Blueprint('routes', __name__)

active_games = {}
top_3 = []


@bp.route('/')
def index():
    return "BattleQuiz API работает!"


@bp.route('/api/quizzes', methods=['GET'])
def get_quizzes():
    quizzes = Quiz.query.all()
    return jsonify([{'id': q.id, 'title': q.title, 'description': q.description, 'image_url': q.image_url}
                    for q in quizzes])


@bp.route('/api/battle/<int:quiz_id>', methods=['GET'])
def get_battle_pair(quiz_id):
    global top_3
    if quiz_id not in active_games:
        # Инициализация новой игры
        items = QuizItem.query.filter_by(quiz_id=quiz_id).all()
        if not items:
            return jsonify({"message": "Викторина пуста"}), 400
        top_3 = []

        item_ids = [item.id for item in items]
        random.shuffle(item_ids)
        king = item_ids.pop() 
        active_games[quiz_id] = {
            'king': king,
            'opponents': item_ids,
            'pair': 0
        }
    game = active_games[quiz_id]
    game['pair'] += 1

    if not game['opponents']:
        final_winner = QuizItem.query.get(game['king'])
        if final_winner:
            final_winner.wins += 1
            db.session.commit()
        del active_games[quiz_id]
        top_3.append({
            'id': final_winner.id,
            'title': final_winner.title,
            'image_url': final_winner.image_url,
        })
        top_3.reverse()
        return jsonify({
            "message": "Победитель определён",
            "winner_id": final_winner.id,
            "image_url": final_winner.image_url,
            "top_3": top_3
        })

    opponent_id = game['opponents'].pop()
    king_item = QuizItem.query.get(game['king'])
    opponent_item = QuizItem.query.get(opponent_id)
    if game['pair'] >= len(Quiz.query.all()):
        top_3.append({
            'id': opponent_item.id,
            'title': opponent_item.title,
            'image_url': opponent_item.image_url,
        })

    battle = BattleRound(
        quiz_id=quiz_id,
        round_number=1, 
        item1_id=king_item.id,
        item2_id=opponent_item.id
    )
    db.session.add(battle)
    db.session.commit()

    return jsonify({
        'battle_id': battle.id,
        'items': [
            {'id': king_item.id, 'image_url': king_item.image_url, 'title': king_item.title},
            {'id': opponent_item.id, 'image_url': opponent_item.image_url, 'title': opponent_item.title}
        ]
    })


@bp.route('/api/vote', methods=['POST'])
def vote():
    data = request.json
    winner_id = data.get('winner_id')
    battle_id = data.get('battle_id')

    if not winner_id or not battle_id:
        return jsonify({'status': 'error', 'message': 'Отсутствуют данные'}), 400

    try:
        battle = BattleRound.query.get(battle_id)
        if not battle:
            return jsonify({'status': 'error', 'message': 'Раунд не найден'}), 404

        if battle.winner_id is not None:
            return jsonify({'status': 'error', 'message': 'Голос уже учтён'}), 400

        if winner_id not in [battle.item1_id, battle.item2_id]:
            return jsonify({'status': 'error', 'message': 'Неверный победитель'}), 400

        battle.winner_id = winner_id
        loser_id = battle.item1_id if winner_id == battle.item2_id else battle.item2_id
        loser = QuizItem.query.get(loser_id)
        if loser:
            loser.losses += 1
        db.session.commit()

        quiz_id = battle.quiz_id
        if quiz_id in active_games:
            game = active_games[quiz_id]
            if winner_id != game['king']:
                game['king'] = winner_id

        return jsonify({'status': 'success'})

    except Exception as e:
        db.session.rollback()
        print(f'Ошибка при голосовании: {e}')
        return jsonify({'status': 'error', 'message': 'Внутренняя ошибка сервера'}), 500


@bp.route('/api/winner/<int:quiz_id>', methods=['GET'])
def get_quiz_winner(quiz_id):
    last_round = db.session.query(func.max(BattleRound.round_number)) \
        .filter(BattleRound.quiz_id == quiz_id).scalar()

    if last_round is None:
        return jsonify({"message": "Турнир ещё не начался"}), 404

    winners = db.session.query(BattleRound.winner_id) \
        .filter_by(quiz_id=quiz_id, round_number=last_round) \
        .filter(BattleRound.winner_id.isnot(None)) \
        .all()

    winner_ids = [w[0] for w in winners if w[0] is not None]

    if len(winner_ids) == 1:
        final_winner = QuizItem.query.get(winner_ids[0])

        if final_winner:
            final_winner.wins += 1
            db.session.commit()

        return jsonify({
            "message": "Финалист определён",
            "winner_id": final_winner.id,
            "image_url": final_winner.image_url,
            "wins": final_winner.wins,
            "losses": final_winner.losses
        })
    else:
        return jsonify({"message": "Финалист ещё не определён", "remaining": winner_ids})


@bp.route('/api/quiz_results/<int:quiz_id>', methods=['GET'])
def quiz_results(quiz_id):
    items = QuizItem.query.filter_by(quiz_id=quiz_id).all()
    results = [{
        'id': item.id,
        'title': item.title,
        'image_url': item.image_url,
        'wins': item.wins,
        'losses': item.losses,
        'score_diff': item.wins - item.losses  
    } for item in items]

    results.sort(key=lambda x: x['wins'], reverse=True)

    top_3_total = sorted(results, key=lambda x: x['wins'], reverse=True)[:3]
    return jsonify({
        "top_3_total": top_3_total
    })
