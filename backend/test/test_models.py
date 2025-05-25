import unittest
from app import create_app
from app.models import db, User, Quiz, QuizItem, BattleRound

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'TESTING': True,
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        })

        with self.app.app_context():                    
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_model(self):
        with self.app.app_context():
            user = User(username="test", email="test@example.com")
            db.session.add(user)
            db.session.commit()
            
            fetched = User.query.first()
            self.assertEqual(fetched.username, "test")
            self.assertEqual(fetched.email, "test@example.com")

    def test_quiz_model(self):
        with self.app.app_context():
            quiz = Quiz(title="Test Quiz", description="Desc", image_url="url.jpg")
            db.session.add(quiz)
            db.session.commit()
            
            fetched = Quiz.query.first()
            self.assertEqual(fetched.title, "Test Quiz")
            self.assertEqual(fetched.description, "Desc")
            self.assertEqual(fetched.image_url, "url.jpg")
            self.assertEqual(fetched.items, [])

    def test_quiz_item_model(self):
        with self.app.app_context():
            quiz = Quiz(title="Test Quiz", description="Desc", image_url="url.jpg")
            db.session.add(quiz)
            db.session.commit()
            
            item = QuizItem(quiz_id=quiz.id, image_url="item.jpg", title="Item 1", wins=5, losses=2)
            db.session.add(item)
            db.session.commit()
            
            fetched = QuizItem.query.first()
            self.assertEqual(fetched.quiz_id, quiz.id)
            self.assertEqual(fetched.wins, 5)
            self.assertEqual(fetched.losses, 2)
            self.assertEqual(fetched.title, "Item 1")

    def test_battle_round_model(self):
        with self.app.app_context():
            quiz = Quiz(title="Test Quiz", description="Desc", image_url="url.jpg")
            item1 = QuizItem(quiz_id=1, image_url="a.jpg", title="A")
            item2 = QuizItem(quiz_id=1, image_url="b.jpg", title="B")
            db.session.add_all([quiz, item1, item2])
            db.session.commit()
            
            battle = BattleRound(
                quiz_id=quiz.id,
                round_number=1,
                item1_id=item1.id,
                item2_id=item2.id
            )
            db.session.add(battle)
            db.session.commit()
            
            fetched = BattleRound.query.first()
            self.assertEqual(fetched.quiz_id, quiz.id)
            self.assertEqual(fetched.round_number, 1)
            self.assertEqual(fetched.item1_id, item1.id)
            self.assertEqual(fetched.item2_id, item2.id)
            self.assertIsNone(fetched.winner_id)
            self.assertIsNone(fetched.loser_id)