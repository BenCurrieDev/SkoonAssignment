from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .views import calculator, database


class CalculatorTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuserunique', password='test1234')
        self.client.login(
            username='testuserunique', password='test1234')

    def test_calculator_view_status_code(self):
        url = reverse('calculator')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_calculator_url_resolves_calculator_view(self):
        view = resolve('/')
        self.assertEquals(view.func, calculator)


class DatabaseTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuserunique', password='test1234')
        self.client.login(
            username='testuserunique', password='test1234')
        url = reverse('database')
        self.response = self.client.get(url)

    def test_database_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_database_url_resolves_database_view(self):
        view = resolve('/database')
        self.assertEquals(view.func, database)
