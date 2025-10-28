from django.db import models

# NoteApp

class Notes(models.Model):
    Note_title = models.CharField(max_length=255)
    Note_desc = models.TextField()


