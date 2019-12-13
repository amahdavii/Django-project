from django.urls import path, re_path, register_converter
from . import views
from extensions import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')


app_name = 'blog'
urlpatterns = [
    #ex: hostname/blog/
    path('', views.index, name = 'index'),

    #ex: hostname/blog/5
    path('<int:post_id>', views.detail, name = 'detail'),
    path('archive/<yyyy:year>/', views.archive_year, name = 'archive')
]