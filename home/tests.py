# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import resolve
from django.test import TestCase
from home.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home_page.html')