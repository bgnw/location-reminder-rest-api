from django.urls import include, path
from .views import (AccountCreate, AccountList, AccountDetail, AccountUpdate, AccountDelete,
                    TaskListCreate, TaskListList, TaskListDetail, TaskListUpdate, TaskListDelete,
                    TaskItemCreate, TaskItemList, TaskItemDetail, TaskItemUpdate, TaskItemDelete)
urlpatterns = [
    path('account/create/', AccountCreate.as_view(), name='create-account'),
    path('account/get', AccountList.as_view()),
    path('account/<str:pk>', AccountDetail.as_view(), name='retrieve-account'),
    path('account/update/<str:pk>', AccountUpdate.as_view(), name='update-account'),
    path('account/delete/<str:pk>', AccountDelete.as_view(), name='delete-account'),

    path('taskl/create/', TaskListCreate.as_view(), name='create-taskl'),
    path('taskl/get', TaskListList.as_view()),
    path('taskl/<str:pk>', TaskListDetail.as_view(), name='retrieve-taskl'),
    path('taskl/update/<str:pk>', TaskListUpdate.as_view(), name='update-taskl'),
    path('taskl/delete/<str:pk>', TaskListDelete.as_view(), name='delete-taskl'),

    path('taski/create/', TaskItemCreate.as_view(), name='create-taski'),
    path('taski/get', TaskItemList.as_view()),
    path('taski/<str:pk>', TaskItemDetail.as_view(), name='retrieve-taski'),
    path('taski/update/<str:pk>', TaskItemUpdate.as_view(), name='update-taski'),
    path('taski/delete/<str:pk>', TaskItemDelete.as_view(), name='delete-taski'),

]

