from django.urls import include, path
from .views import TaskListCreate, TaskListList, TaskListDetail, TaskListUpdate, TaskListDelete

urlpatterns = [
    path('create/', TaskListCreate.as_view(), name='create-taskl'),
    path('get', TaskListList.as_view()),
    path('<int:pk>', TaskListDetail.as_view(), name='retrieve-taskl'),
    path('update/<str:pk>', TaskListUpdate.as_view(), name='update-taskl'),
    path('delete/<str:pk>', TaskListDelete.as_view(), name='delete-taskl'),
]
