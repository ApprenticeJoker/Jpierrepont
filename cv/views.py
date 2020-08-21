# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import CVSection

# Create your views here.
def cv_view(request):
    CVSections = CVSection.objects.filter()
    return render(request, 'cv_view.html', {'CVSections': CVSections})