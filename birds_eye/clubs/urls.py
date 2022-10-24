from django.urls import path
from . import views

app_name = "clubs"

urlpatterns = [
    path('', views.ClubListView.as_view(), name="all"),
    path('<int:pk>/', views.ClubDetailView.as_view(), name="club-detail"),
]