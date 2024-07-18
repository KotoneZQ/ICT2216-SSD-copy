from django.test import TestCase, SimpleTestCase
from .models import Users
from django.urls import reverse, resolve
from .forms import RegisterForm
from .views import home_view, login_view
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersModelTest(TestCase):
    def setUp(self):
        self.user = Users.objects.create(
            username='testuser',
            password_hash='testpassword',
            email='testuser@example.com'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.is_active)


class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class LoginViewTest(TestCase):
    def test_login_view_status_code(self):
        response = self.client.get(reverse('login_view'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template_used(self):
        response = self.client.get(reverse('login_view'))
        self.assertTemplateUsed(response, 'login.html')


class RegisterFormTest(TestCase):
    def test_register_form_valid(self):
        form = RegisterForm(data={
            'uname': 'testuser',
            'email': 'testuser@example.com',
            'psw': 'testpassword'
        })
        self.assertTrue(form.is_valid())

    def test_register_form_invalid(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())


class URLTests(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_view)

    def test_login_url_is_resolved(self):
        url = reverse('login_view')
        self.assertEqual(resolve(url).func, login_view)


class UserRegistrationIntegrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('register_view'), {
            'uname': 'integrationtestuser',
            'email': 'integrationtestuser@example.com',
            'psw': 'integrationtestpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        user = Users.objects.get(username='integrationtestuser')
        self.assertIsNotNone(user)


class AuthenticationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        response = self.client.post(reverse('login_view'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)