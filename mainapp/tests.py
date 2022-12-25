from django.test import TestCase, Client
from django.urls import reverse
from http import HTTPStatus
from mainapp.models import News
from authapp.models import User
from authapp import models as authapp_models
from mainapp import tasks as mainapp_tasks
from django.core import mail as django_mail


class StaticPagesSmokeTest(TestCase):

    def test_page_index_open(self):
        url = reverse('mainapp:index')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_page_contacts_open(self):
        url = reverse('mainapp:contacts')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)


class NewsTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        for i in range(10):
            News.objects.create(
                title=f'News{i}',
                preamble=f'Preamble{i}',
                body=f'Body{i}'
            )
        User.objects.create_superuser(username='django', password='geekbrains')
        self.client_with_auth = Client()
        auth_url = reverse('authapp:login')
        self.client_with_auth.post(
            {'username': 'django', 'password': 'geekbrains'}
        )

    def test_open_page(self):
        url = reverse('mainapp:news')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_failed_open_add_by_anonym(self):
        url = reverse('mainapp:news_create')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.FOUND)

    def test_create_news_item_by_admin(self):

        news_count = News.objects.all().count()

        url = reverse('mainapp:news_create')
        result = self.client_with_auth.post(
            url,
            data={
                'title': 'Test news',
                'preamble': 'Test preamble',
                'body': 'Test body'
            }
        )

        self.assertEqual(result.status_code, HTTPStatus.FOUND)

        self.assertEqual(News.objects.all().count(), news_count)


class TestTaskMailSend(TestCase):
    fixtures = ("authapp/fixtures/user_admin.json",)

    def test_mail_send(self):
        message_text = "test_message_text"
        user_obj = authapp_models.User.objects.first()
        mainapp_tasks.send_feedback_to_email(
            {"user_id": user_obj.id, "message": message_text})
        self.assertEqual(django_mail.outbox[0].body, message_text)
