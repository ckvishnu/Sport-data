from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('add_details',views.add),
    path('display_data',views.display),
]