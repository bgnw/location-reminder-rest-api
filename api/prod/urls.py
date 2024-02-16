from django.urls import include, path
from .views import AccountCreate, AccountList, AccountDetail, AccountUpdate, AccountDelete, TaskListCreate, TaskListList, TaskItemCreate, TaskItemList

urlpatterns = [
    path('create/', AccountCreate.as_view(), name='create-account'),
    path('', AccountList.as_view()),
    path('<int:pk>', AccountDetail.as_view(), name='retrieve-account'),
    path('update/<int:pk>', AccountUpdate.as_view(), name='update-account'),
    path('delete/<int:pk>', AccountDelete.as_view(), name='delete-account')
]

