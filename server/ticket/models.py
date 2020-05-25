from django.db import models

# Create your models here.
class Ticket(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=140)
    description = models.TextField()

    def __str__(self):
        return self.title