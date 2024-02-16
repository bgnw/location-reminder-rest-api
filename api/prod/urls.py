from django.urls import include, path
from .views import AccountCreate, AccountList, AccountDetail, AccountUpdate, AccountDelete, TaskListCreate, TaskListList, TaskItemCreate, TaskItemList

urlpatterns = [
    path('create/', AccountCreate.as_view(), name='create-account'),
    path('', AccountList.as_view()),
    path('<str:pk>', AccountDetail.as_view(), name='retrieve-account'),
    path('update/<str:pk>', AccountUpdate.as_view(), name='update-account'),
    path('delete/<str:pk>', AccountDelete.as_view(), name='delete-account')
]

