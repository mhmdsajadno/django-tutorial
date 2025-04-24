from django.contrib import admin
from django.urls import path
from bookshelf import views as bookViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bookViews.index),
    path('home/',bookViews.home)
]
