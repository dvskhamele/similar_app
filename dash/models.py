# -*- coding: utf-8 -*
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import slugify

class Appli(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)


    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Appli, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

