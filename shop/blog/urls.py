from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    #ex: hostname/blog/
    path('', views.index, name = 'index'),

    #ex: hostname/blog/5
    path('<int:post_id>', views.detail, name = 'detail'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.archive_year, name = 'archive')
]