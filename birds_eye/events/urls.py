from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.EntireCalendar.as_view(), name="entire"),
]