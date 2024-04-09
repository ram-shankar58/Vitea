from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()



class Notes(models.Model):
    branch = [
        ('CSE', 'CSE'),
        ('IT','IT'),
        ('EEE', 'EEE'),
        ('ECE', 'ECE'),
        ('Mechanical', 'Mechanica;'),
        ('Civil', 'Civil'),
        ('Law', 'Law'),
        ('Fashion', 'Fashion'),
        ('Business', 'Business'),
    ]
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    content = models.FileField(upload_to='notes/')
    branch = models.CharField(max_length=50, choices=branch, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    