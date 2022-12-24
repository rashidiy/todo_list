from django.db.models import Model, CharField, BooleanField


# Create your models here.

class Task(Model):
    title = CharField(max_length=255)
    description = CharField(max_length=1024, blank=True, null=True)
    status = BooleanField(default=False)