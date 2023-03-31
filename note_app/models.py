from django.db import models
from django.utils.timezone import now

# Create your models here.


class NoteModel(models.Model):
    date_created = models.DateTimeField(default=now())
    note_name = models.CharField(max_length=50, default="")
    note_text = models.TextField(max_length=500)
    
    #urgency = models.Choices()

