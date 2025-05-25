from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    items = db.relationship('QuizItem', backref='quiz', lazy=True)


class QuizItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    image_url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)


class BattleRound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    round_number = db.Column(db.Integer, nullable=False)
    item1_id = db.Column(db.Integer, db.ForeignKey('quiz_item.id'), nullable=False)
    item2_id = db.Column(db.Integer, db.ForeignKey('quiz_item.id'), nullable=False)
    winner_id = db.Column(db.Integer, db.ForeignKey('quiz_item.id'))
    loser_id = db.Column(db.Integer, db.ForeignKey('quiz_item.id'))

