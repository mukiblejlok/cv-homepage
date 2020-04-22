from . import LoginTestCase, LOGIN_PATHS


class TestRoutes(LoginTestCase):

    def test_redirect_when_not_logged_in(self):
        _target = "/auth/login"
        for path in LOGIN_PATHS:
            response = self.client.get(path)
            self.assertRedirects(response, _target, query={"next": [path]})

    def test_404(self):
        invalid_paths = ["/ss", "/rds", "/new-asset-reports", '/api/sss']
        for path in invalid_paths:
            response = self.client.get(path)
            self.assert_404(response)
