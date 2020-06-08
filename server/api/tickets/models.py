from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Ticket(models.Model):
    completed = models.BooleanField(default=False)
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=240, blank=True)
    reply_to = models.EmailField(blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.title