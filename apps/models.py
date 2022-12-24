from django.contrib.auth.models import User
from django.db.models import Model, CharField, BooleanField, ForeignKey, CASCADE


# Create your models here.

class Task(Model):
    user = ForeignKey(User, CASCADE)
    title = CharField(max_length=255)
    description = CharField(max_length=1024, blank=True, null=True)
    status = BooleanField(default=False)
