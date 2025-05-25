import unittest
from app import create_app
from app.models import db, Quiz, QuizItem, BattleRound
import json

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'TESTING': True,
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        })
        
        
        with self.app.app_context():
            db.create_all()
            
            quiz = Quiz(title="Test Quiz", description="Test", image_url="quiz.jpg")
            db.session.add(quiz)
            
            items = [
                QuizItem(quiz_id=1, image_url="a.jpg", title="A"),
                QuizItem(quiz_id=1, image_url="b.jpg", title="B"),
                QuizItem(quiz_id=1, image_url="c.jpg", title="C")
            ]
            db.session.add_all(items)
            db.session.commit()

        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "BattleQuiz API работает!")

    def test_get_quizzes(self):
        response = self.client.get('/api/quizzes')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Test Quiz")

    def test_get_battle_pair(self):
        response = self.client.get('/api/battle/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('battle_id', data)
        self.assertEqual(len(data['items']), 2)

    def test_get_battle_pair_invalid_quiz(self):
        response = self.client.get('/api/battle/999')
        self.assertEqual(response.status_code, 400)

    def test_vote(self):
        with self.app.app_context():
            battle = BattleRound(
                quiz_id=1,
                round_number=1,
                item1_id=1,
                item2_id=2
            )
            db.session.add(battle)
            db.session.commit()
            
            response = self.client.post('/api/vote', json={
                'winner_id': 1,
                'battle_id': battle.id
            })
            self.assertEqual(response.status_code, 200)
            
            updated_battle = BattleRound.query.get(battle.id)
            self.assertEqual(updated_battle.winner_id, 1)

    def test_vote_invalid_data(self):
        response = self.client.post('/api/vote', json={})
        self.assertEqual(response.status_code, 400)

    def test_get_quiz_winner(self):
        with self.app.app_context():
            response = self.client.get('/api/winner/1')
            self.assertEqual(response.status_code, 404)
            
            battle = BattleRound(
                quiz_id=1,
                round_number=1,
                item1_id=1,
                item2_id=2,
                winner_id=1,
                loser_id=2
            )
            db.session.add(battle)
            db.session.commit()
            
            response = self.client.get('/api/winner/1')
            self.assertEqual(response.status_code, 200)

    def test_quiz_results(self):
        response = self.client.get('/api/quiz_results/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['top_3_total']), 3)