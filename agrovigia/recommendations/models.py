# encoding: utf-8
from __future__ import unicode_literals
from django.db import models

from vegetables.models import Vegetable


class Recommendation(models.Model):
    vegetable = models.ForeignKey(Vegetable)
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    message = models.TextField(blank=False)

    def __unicode__(self):
        return self.vegetable.name
