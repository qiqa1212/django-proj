from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.models import User

class Topic(models.Model):
     text = models.CharField(max_length=200)
     date_added = models.DateTimeField(auto_now_add=True)
     owner = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
         return self.text




class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text