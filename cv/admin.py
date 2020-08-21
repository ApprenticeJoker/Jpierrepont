# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import CVSection
from .models import CVSubsection

admin.site.register(CVSection)
admin.site.register(CVSubsection)