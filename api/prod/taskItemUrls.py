from django.urls import include, path
from .views import TaskItemCreate, TaskItemList, TaskItemDetail, TaskItemUpdate, TaskItemDelete, TaskItemSearchListID, TaskItemSearchOwner, ItemOpportunityLookup

urlpatterns = [
    path('create/', TaskItemCreate.as_view(), name='create-taski'),
    path('get', TaskItemList.as_view()),
    path('from-list/<int:list_id>', TaskItemSearchListID.as_view(), name='from-list-taski'),
    path('from-user/<str:username>', TaskItemSearchOwner.as_view(), name='from-user-taski'),
    path('<int:pk>', TaskItemDetail.as_view(), name='retrieve-taski'),
    path('update/<int:pk>', TaskItemUpdate.as_view(), name='update-taski'),
    path('delete/<int:pk>', TaskItemDelete.as_view(), name='delete-taski'),
    path('opps/<int:item_id>', ItemOpportunityLookup.as_view(), name='iopp-lookup'),
    path('opps/create/', ItemOpportunityLookup.as_view(), name='iopp-lookup'),
]
