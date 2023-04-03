from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.


class NoteModel(models.Model):
    date_created = models.DateTimeField(default=now())
    note_name = models.CharField(max_length=50, default="")
    note_text = models.TextField(max_length=500)
    user = models.ForeignKey(User, default="", null=True, blank=True, on_delete=models.CASCADE)
    
    #urgency = models.Choices()

