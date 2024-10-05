from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:current_course>', views.query, name='query'),
    # path('<str:current_course>/take', views.take, name='take'),
    path('', views.index, name='index_return'),
    path('<int:taking_id>', views.query, name='query'),
    path('<int:taking_id>/take', views.take, name='take'),
]