from django.urls import include, path
from .views import TaskListCreate, TaskListList, TaskListDetail, TaskListUpdate, TaskListDelete, TaskListSearchOwner

urlpatterns = [
    path('create/', TaskListCreate.as_view(), name='create-taskl'),
    path('get', TaskListList.as_view()),
    path('<int:pk>', TaskListDetail.as_view(), name='retrieve-taskl'),
    path('from-user/<str:username>', TaskListSearchOwner.as_view(), name='from-user-taskl'),
    path('update/<str:pk>', TaskListUpdate.as_view(), name='update-taskl'),
    path('delete/<str:pk>', TaskListDelete.as_view(), name='delete-taskl'),
]
