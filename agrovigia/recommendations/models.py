# encoding: utf-8
from __future__ import unicode_literals
from django.db import models

from vegetables.models import Vegetable


class Recommendation(models.Model):
    vegetable_id = models.ForeignKey(Vegetable)
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()
    message = models.TextField(blank=False)

    def __unicode__(self):
        return self.vegetable_id.name
