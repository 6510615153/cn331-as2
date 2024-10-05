from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:current_course>', views.query, name='query'),
    #path('<str:name>', views.take, name='take'),
]