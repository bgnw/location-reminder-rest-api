from django.urls import include, path
from .views import *

urlpatterns = [
    path('create/', TaskItemCreate.as_view(), name='create-taski'),
    path('get', TaskItemList.as_view()),
    path('from-list/<int:list_id>', TaskItemSearchListID.as_view(), name='from-list-taski'),
    path('from-user/<str:username>', TaskItemSearchOwner.as_view(), name='from-user-taski'),
    path('<int:pk>', TaskItemDetail.as_view(), name='retrieve-taski'),
    path('update/<int:pk>', TaskItemUpdate.as_view(), name='update-taski'),
    path('delete/<int:pk>', TaskItemDelete.as_view(), name='delete-taski'),
    path('opps/', ItemOpportunityList.as_view(), name='iopp-list'),
    path('opps/<int:item_id>', ItemOpportunityLookup.as_view(), name='iopp-lookup'),
    path('opps/create/', ItemOpportunityCreate.as_view(), name='iopp-create'),

    path('filters-add', FilterCreate.as_view(), name='filters-add'),
    path('filters-list', FilterList.as_view(), name='filters-list'),
    path('filters-foritem/<int:item>', FiltersForItem.as_view(), name='filters-foritem'),
    path('filters-update/<int:entry_id>', FilterUpdate.as_view(), name='filters-update'),
    path('filters-delete/<int:entry_id>', FilterDelete.as_view(), name='filters-delete'),
]
