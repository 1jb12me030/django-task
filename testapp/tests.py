import time
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Question, Answer

# Optional: Time logger for tests
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Time taken for {func.__name__}: {duration:.4f} seconds")
        return result
    return wrapper


class QuoraAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    @log_time
    def test_signup_view(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'newpass1234',
            'password2': 'newpass1234'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    @log_time
    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)

    @log_time
    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('logout'))  # Must be POST
        self.assertEqual(response.status_code, 302)

    @log_time
    def test_ask_question_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('ask'), {
            'title': 'Test Question',
            'description': 'This is a test question body'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Question.objects.filter(title='Test Question').exists())

    @log_time
    def test_question_list_view(self):
        Question.objects.create(title='Q1', description='Body1', author=self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Q1')

    @log_time
    def test_like_answer_view(self):
        self.client.login(username='testuser', password='testpass')

        question = Question.objects.create(
            title='Test Like Question',
            description='Question description',
            author=self.user
        )

        answer_author = User.objects.create_user(username='answeruser', password='answerpass')
        answer = Answer.objects.create(
            question=question,
            content='Sample answer content',
            author=answer_author
        )

        response = self.client.get(reverse('like_answer', args=[answer.id]))
        self.assertEqual(response.status_code, 302)
        answer.refresh_from_db()
        self.assertIn(self.user, answer.likes.all())
