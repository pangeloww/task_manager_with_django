from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.forms import CreateTask, DeleteTask
from tasks.models import Task


class CreateTaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('create_task')

    def test_get_request(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CreateTask)

    def test_post_valid_data(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            # invalid data
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertTrue(Task.objects.filter(assigned_to=self.user).exists())

    def test_post_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            # invalid data
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(assigned_to=self.user).exists())


class EditTaskViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='Test Task', description='Test Description')
        self.url = reverse('edit_task', args=[self.task.pk])

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CreateTask)

    def test_post_valid_data(self):
        data = {
            # invalid data
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()

    def test_post_invalid_data(self):
        data = {
            # invalid data
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)

class DeleteTaskViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='Test Task', description='Test Description')
        self.url = reverse('delete_task', args=[self.task.pk])

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], DeleteTask)

    def test_post_valid_data(self):
        data = {
            # Include valid form data for confirming task deletion
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
