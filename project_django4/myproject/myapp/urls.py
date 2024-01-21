#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:08:17 2024

@author: arun
"""

# myapp/urls.py
from django.urls import path
from .views import (
    simple_response, redirect_example, permanent_redirect_example,
    not_modified_example, bad_request_example, forbidden_example,
    not_allowed_example, gone_example, server_error_example,
    not_found_example, json_response_example, streaming_response, serve_file
)

urlpatterns = [
    path('simple/', simple_response, name='simple_response'),
    path('redirect/', redirect_example, name='redirect_example'),
    path('permanent_redirect/', permanent_redirect_example, name='permanent_redirect_example'),
    path('not_modified/', not_modified_example, name='not_modified_example'),
    path('bad_request/', bad_request_example, name='bad_request_example'),
    path('forbidden/', forbidden_example, name='forbidden_example'),
    path('not_allowed/', not_allowed_example, name='not_allowed_example'),
    path('gone/', gone_example, name='gone_example'),
    path('server_error/', server_error_example, name='server_error_example'),
    path('not_found/', not_found_example, name='not_found_example'),
    path('json_response/', json_response_example, name='json_response_example'),
    path('streaming/', streaming_response, name='streaming_response'),
    path('serve_file/', serve_file, name='serve_file'),
]
