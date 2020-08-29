from django.db import models
from django.utils import timezone


class Yazı(models.Model):
    yazi = models.TextField()
    tarih = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.yazi.partition('\n')[0])