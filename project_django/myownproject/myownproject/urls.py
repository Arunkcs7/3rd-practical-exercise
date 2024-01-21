# myownproject/urls.py
from django.contrib import admin
from django.urls import path, include
from helloapp.views import hello_world  # Correct the import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloapp/', include('helloapp.urls')),
]


