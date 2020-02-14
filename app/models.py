from django.db import models
from django.urls import reverse
import datetime


class AddPost(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=500)
    username = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    def save(self):
        if not self.id:
            self.time = datetime.datetime.now()
        self.time = datetime.datetime.now()
        super(AddPost, self).save()

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    def __str__(self):
        return self.category
