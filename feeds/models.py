from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse


class Thought(models.Model):
    content = models.TextField(max_length=255, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("feed-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f'Thought by {self.author}: {self.content[:20]}...'
