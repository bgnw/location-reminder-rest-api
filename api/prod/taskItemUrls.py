from django.urls import include, path
from .views import TaskItemCreate, TaskItemList, TaskItemDetail, TaskItemUpdate, TaskItemDelete

urlpatterns = [
    path('taski/create/', TaskItemCreate.as_view(), name='create-taski'),
    path('taski/get', TaskItemList.as_view()),
    path('taski/<str:pk>', TaskItemDetail.as_view(), name='retrieve-taski'),
    path('taski/update/<str:pk>', TaskItemUpdate.as_view(), name='update-taski'),
    path('taski/delete/<str:pk>', TaskItemDelete.as_view(), name='delete-taski'),
]
