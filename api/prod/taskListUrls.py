from django.urls import include, path
from .views import TaskListCreate, TaskListList, TaskListDetail, TaskListUpdate, TaskListDelete

urlpatterns = [
    path('taskl/create/', TaskListCreate.as_view(), name='create-taskl'),
    path('taskl/get', TaskListList.as_view()),
    path('taskl/<str:pk>', TaskListDetail.as_view(), name='retrieve-taskl'),
    path('taskl/update/<str:pk>', TaskListUpdate.as_view(), name='update-taskl'),
    path('taskl/delete/<str:pk>', TaskListDelete.as_view(), name='delete-taskl'),
]
