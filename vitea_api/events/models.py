from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Event(models.Model):
    
    title=models.Charfield(max_length=255)
    description=models.TextField(null=False, blank=False)
    content=models.ImageField(upload_to='events/', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    club=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


    def user_check(self, user):
        return user.role=='CL'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.user_check(self, self.club):
                raise Exception("Only clubs can post")
        
        super.save(*args, **kwargs)

    