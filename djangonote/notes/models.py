# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    text = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text


