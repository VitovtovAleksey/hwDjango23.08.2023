from django.urls import path
from . import views
from datetime import datetime

urlpatterns = [
   path("", views.index),
   # path("contacts/", views.contacts),
   path("day/", views.day),
   path("date/", views.date),
   path("holiday/", views.holiday),
   path("table/", views.table)


]