from django.test import RequestFactory

from test_plus.test import TestCase

from ..views import PeriodCreate, PeriodUpdate

class BaseUserTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory

class TestPeriodCreateView(BaseUserTestCase):

    def setUp(self):
        super(TestPeriodCreateView, self).setUp()
        self.view = PeriodCreate()
        request = self.factory.get('/fake-url')
        request.user = self.user
        self.view.request = request

    def test_get_success_url(self):
        self.assertEqual(
            self.view.get_success_url(),
            '/fertility/periods/'
        )

    def test_get_object(self):
        self.assertEqual()


class TestPeriodUpdateView(BaseUserTestCase):
    pass




