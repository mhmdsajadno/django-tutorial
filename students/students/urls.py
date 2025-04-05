from django.contrib import admin
from django.urls import path
from app import views as appView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", appView.index, name="home"),
    path("menu/<int:id>/", appView.menu, name="menu"),
    path('search/', appView.search, name='search')
]
