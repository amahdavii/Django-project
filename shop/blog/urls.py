from django.urls import path
from . import views

urlpatterns = [
    #ex: hostname/blog/
    path('', views.index, name = 'index'),

    #ex: hostname/blog/5
    path('<int:post_id>', views.detail, name = 'detail'),
]