from flask.helpers import url_for
from flask_testing import TestCase
from flask import current_app
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def testAppInTestMode(self):
        self.assertTrue(current_app.config['TESTING'])

    def testIndexRedirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response,url_for('hello'))

    def testHelloGet(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)

    def testHelloPost(self):
        fakeForm = {
            'username' : 'fake',
            'password' : 'fakePassword'
        }
        response = self.client.post(url_for('hello'),data=fakeForm)
        self.assertRedirects(response,url_for('index'))