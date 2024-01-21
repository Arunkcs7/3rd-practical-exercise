#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 02:18:33 2024

@author: arun
"""
from django.urls import path
from .views import hello_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
]