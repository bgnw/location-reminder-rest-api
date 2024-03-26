from django.urls import include, path
from .views import *

urlpatterns = [
    path('add/', LogAdd.as_view(), name='log-add'),
    path('get', LogList.as_view()),
]
