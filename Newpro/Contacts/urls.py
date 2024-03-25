from django.urls import path
from .import views

urlpatterns =[
    path('contc',views.hoe,name="contc"),
]