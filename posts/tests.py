from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(username = "testuser", password="testpass123")
        testuser.save()

        post = Post.objects.create(author = testuser, title = "a title", body = "a body")
        post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'a title')
        self.assertEqual(body, 'a body')
