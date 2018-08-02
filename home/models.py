# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #user=models.ForeignKey(User)
    date=models.DateTimeField(auto_now=True)
    text=models.TextField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
