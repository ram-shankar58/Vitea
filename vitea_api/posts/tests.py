from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post, Comment
from django.contrib.auth import get_user_model
 
class PostModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_create_post(self):
        post = Post.objects.create(
            title='Test title',
            content=SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"),
            upvotes=10,
            downvotes=2,
            author=self.user
        )
        self.assertEqual(post.title, 'Test title')
        self.assertEqual(post.upvotes, 10)
        self.assertEqual(post.downvotes, 2)
        self.assertEqual(post.author, self.user)


class CommentModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test title',
            content=SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"),
            upvotes=10,
            downvotes=2,
            author=self.user
        )

    def test_create_comment(self):
        comment = Comment.objects.create(
            content='Test comment',
            post=self.post,
            author=self.user
        )
        self.assertEqual(comment.content, 'Test comment')
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.author, self.user)

    def test_create_nested_comment(self):
        parent_comment = Comment.objects.create(
            content='Test parent comment',
            post=self.post,
            author=self.user
        )
        child_comment = Comment.objects.create(
            content='Test child comment',
            post=self.post,
            author=self.user,
            parent=parent_comment
        )
        self.assertEqual(child_comment.content, 'Test child comment')
        self.assertEqual(child_comment.post, self.post)
        self.assertEqual(child_comment.author, self.user)
        self.assertEqual(child_comment.parent, parent_comment)