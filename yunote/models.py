from django.conf import settings
from django.db import models as m
from django.urls import reverse


# Create your models here.

class Note(m.Model):
    user = m.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m.CASCADE)
    title = m.CharField(max_length=120)
    file = m.FileField(null=True, blank=True)
    note = m.TextField(null=True, blank=True)
    timestamp = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_delete_url(self):
        return reverse("notes:delete", kwargs={
            "id": self.id
        })

    def get_update_url(self):
        return reverse("notes:update", kwargs={
            "id": self.id
        })
