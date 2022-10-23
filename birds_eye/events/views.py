from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic 
from django.shortcuts import get_object_or_404
from events.models import Event
from . import models

class EntireCalendar(generic.ListView):
    model = Event