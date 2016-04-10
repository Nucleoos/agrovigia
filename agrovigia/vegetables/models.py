# encoding: utf-8
from __future__ import unicode_literals

from django.db import models


class Vegetable(models.Model):
    short_name = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=30, blank=False)

    def __unicode__(self):
            return self.name
