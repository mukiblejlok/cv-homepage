import urllib
import warnings

from flask import Response
from flask_testing import TestCase

from app import create_app, db

from app.models.user import User

test_user = User(id=1001,
                 first_name="Test",
                 last_name="User",
                 email="test.user@fmularczyk.pl",
                 is_web_admin=False)

admin_user = User(id=2001,
                  first_name="Mr",
                  last_name="Admin",
                  email="admin@fmularczyk.pl",
                  is_web_admin=True)

LOGIN_PATHS = [
    "/admin/"
]
NO_LOGIN_PATHS = [
    "/",
    "/auth/login",
    "/cv/",
    "/api/version"
]
ALL_PATHS = LOGIN_PATHS + NO_LOGIN_PATHS


class LoginTestCase(TestCase):

    def create_app(self):
        warnings.simplefilter('ignore', category=DeprecationWarning)
        app = create_app('testing')
        app_context = app.app_context()
        app_context.push()
        db.create_all()
        return app

    def assertRedirects(self, response: Response, path: str, query: dict = None, mode: str = "local"):
        query = query if query is not None else {}
        if mode == "direct":
            self.assertEqual(response.location, path)
        else:
            parsed_url = urllib.parse.urlparse(response.location)
            parsed_query = urllib.parse.parse_qs(parsed_url.query)
            self.assertEqual(parsed_url.path, path)
            self.assertEqual(parsed_query, query)

    def assertInHTML(self, text: str, response: Response):
        html_response = str(response.data, encoding='utf-8')
        self.assertIn(text, html_response)

    def assertNotInHTML(self, text: str, response: Response):
        html_response = str(response.data, encoding='utf-8')
        self.assertNotIn(text, html_response)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class NoLoginTestCase(LoginTestCase):
    def create_app(self):
        warnings.simplefilter('ignore', category=DeprecationWarning)
        app = create_app('no_login_test')
        app_context = app.app_context()
        app_context.push()
        db.create_all()
        return app
