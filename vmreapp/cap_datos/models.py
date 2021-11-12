
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class votos(models.Model):
    partido = models.CharField(max_length=20)
    voto_postal = models.IntegerField(max_length=33)
    voto_internet = models.IntegerField(max_length=33)