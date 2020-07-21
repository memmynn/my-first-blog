from django.db import models
from django.utils import timezone


class Yazi(models.Model):
    yazar = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    yazi = models.TextField()
    tarih = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()
