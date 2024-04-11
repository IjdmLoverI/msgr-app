from django.contrib.auth.models import User
from django.db import models


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='participants')

    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    sent_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Message from {self.sender.username}"
