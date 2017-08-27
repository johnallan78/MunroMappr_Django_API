# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from .models import Mountain

# Create your views here.


class IndexView(generic.ListView):
  model = Mountain
  # automatically goes to template folder
  template_name = 'index.html'

    # def get_queryset(self):
    #   return Mountain.objects