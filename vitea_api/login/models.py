from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STUDENT = 'ST'
    MODERATOR = 'MO'
    TEACHER = 'TE'
    ALUMNI = 'AL'
    CLUB = 'CL'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (MODERATOR, 'Moderator'),
        (TEACHER, 'Teacher'),
        (ALUMNI, 'Alumni'),
        (CLUB, 'Club')
    ]

    SEX_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Prefer not to say")
    )

    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=STUDENT,
    )

    campus = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=20)
    regno = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES)

    @property
    def year(self):
        return int("20"+self.regno[:2])
