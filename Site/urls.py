from django.urls import path
from Site import views

urlpatterns = [
    path('hello/',views.Welcome),
]
