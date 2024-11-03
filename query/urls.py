from django.urls import path
from . import views

app_name = "query"

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index_return'),
    path('<int:taking_id>', views.query, name='query_id'),
    path('<int:taking_id>/take', views.take, name='take'),
    path('check', views.check, name='check'),
]