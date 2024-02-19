from django.urls import include, path
from .views import TaskItemCreate, TaskItemList, TaskItemDetail, TaskItemUpdate, TaskItemDelete

urlpatterns = [
    path('create/', TaskItemCreate.as_view(), name='create-taski'),
    path('get', TaskItemList.as_view()),
    path('<str:pk>', TaskItemDetail.as_view(), name='retrieve-taski'),
    path('update/<str:pk>', TaskItemUpdate.as_view(), name='update-taski'),
    path('delete/<str:pk>', TaskItemDelete.as_view(), name='delete-taski'),
]
