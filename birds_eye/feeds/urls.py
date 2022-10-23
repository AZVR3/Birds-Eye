from django.urls import path
from . import views

app_name = "feeds"

urlpatterns = [
    path("", views.ListFeeds.as_view(), name="all"),
]