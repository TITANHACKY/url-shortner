from django.contrib import admin
from django.urls import path

from API.views import display_url, add_short_url

urlpatterns = [
    path('url/<str:short_code>/', display_url),
    path('short-url/', add_short_url),
]