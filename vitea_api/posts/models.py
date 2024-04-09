from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Post(models.Model):

    boards = [
        ('General', 'General'),
        ('Academic', 'Academic'),
        ('Entertainment', 'Entertainment'),
        ('Sports', 'Sports'),
        ('Politics', 'Politics'),
        ('Religion', 'Religion'),
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Fashion', 'Fashion'),
        ('Business', 'Business'),
        ('Science', 'Science'),
        ('Agriculture', 'Agriculture'),
        ('Hackclub', 'Hackclub'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    content = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.CharField(max_length=255, choices=boards, default='General')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.content