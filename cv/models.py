# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CVSection(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class CVSubsection(models.Model):
    section = models.ForeignKey('cv.CVSection', on_delete=models.CASCADE, related_name='subsections')
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title