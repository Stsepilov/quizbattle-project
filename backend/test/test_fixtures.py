import unittest
from app import create_app
from app.models import db, Quiz, QuizItem, BattleRound

class TestFixtures(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'TESTING': True,
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        })
        
        
        with self.app.app_context():
            db.create_all()
            
            self.quiz = Quiz(title="Test Quiz", description="Test", image_url="quiz.jpg")
            db.session.add(self.quiz)
            
            self.item1 = QuizItem(quiz_id=1, image_url="a.jpg", title="A")
            self.item2 = QuizItem(quiz_id=1, image_url="b.jpg", title="B")
            db.session.add_all([self.item1, self.item2])
            
            self.battle = BattleRound(
                quiz_id=1,
                round_number=1,
                item1_id=1,
                item2_id=2
            )
            db.session.add(self.battle)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_quiz_relationships(self):
        with self.app.app_context():
            quiz = Quiz.query.get(1)
            self.assertEqual(len(quiz.items), 2)
            self.assertEqual(quiz.items[0].title, "A")

    def test_item_defaults(self):
        with self.app.app_context():
            item = QuizItem.query.get(1)
            self.assertEqual(item.wins, 0)
            self.assertEqual(item.losses, 0)

    def test_battle_initialization(self):
        with self.app.app_context():
            battle = BattleRound.query.get(1)
            self.assertEqual(battle.quiz_id, 1)
            self.assertEqual(battle.round_number, 1)
            self.assertEqual(battle.item1_id, 1)
            self.assertEqual(battle.item2_id, 2)
            self.assertIsNone(battle.winner_id)
            self.assertIsNone(battle.loser_id)