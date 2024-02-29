from django.urls import include, path
from .views import TaskItemCreate, TaskItemList, TaskItemDetail, TaskItemUpdate, TaskItemDelete, TaskItemSearchListID

urlpatterns = [
    path('create/', TaskItemCreate.as_view(), name='create-taski'),
    path('get', TaskItemList.as_view()),
    path('from-list/<int:pk>', TaskItemSearchListID.as_view(), name='from-list-taski'),
    path('<int:pk>', TaskItemDetail.as_view(), name='retrieve-taski'),
    path('update/<int:pk>', TaskItemUpdate.as_view(), name='update-taski'),
    path('delete/<int:pk>', TaskItemDelete.as_view(), name='delete-taski'),
]
