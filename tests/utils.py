import unittest
from datetime import datetime

from app.api import app
from run import create_app, models

actors_data = [
    {'first_name': 'Anya', 'last_name': 'Barrick', 'age': 26, 
    'gender': 'FEMALE'},
    {'first_name': 'Alisa', 'last_name': 'Caddi', 'age': 32,
    'gender': 'FEMALE'},
    {'first_name': 'Ema', 'last_name': 'Forth', 'age': 22,
    'gender': 'FEMALE'},
    {'first_name': 'Henry', 'last_name': 'Hartmann', 'age': 25,
    'gender': 'MALE'},
    {'first_name': 'David', 'last_name': 'Posch', 'age': 24,
    'gender': 'MALE'},
    {'first_name': 'Gary', 'last_name': 'Leap', 'age': 26,
    'gender': 'MALE'},
]

movies_data = [
    {'title': 'Lions Heart', 'release_date': datetime(2020, 12, 1)},
    {'title': 'The Old Guard', 'release_date': datetime(2020, 7, 15)},
    {'title': 'Baby Boom', 'release_date': datetime(2021, 3, 11)},
]

TEST_DB_CONFIG = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite://',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}


class TestAgencyMixin(unittest.TestCase):
    @staticmethod
    def _create_test_data():
        for data in actors_data:
            models.Actor(**data).insert()
        for data in movies_data:
            models.Movie(**data).insert()

    def setUp(self):
        self.app = create_app('test.log', app.LOGGER, TEST_DB_CONFIG)
        self.client = self.app.test_client
        self.app.app_context().push()
        models.db.init_app(self.app)
        models.db.create_all()
        self._create_test_data()

    def tearDown(self):
        models.db.session.remove()
        models.db.drop_all()
