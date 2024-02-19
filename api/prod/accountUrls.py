from django.urls import include, path
from .views import AccountCreate, AccountList, AccountDetail, AccountUpdate, AccountDelete

urlpatterns = [
    path('account/create/', AccountCreate.as_view(), name='create-account'),
    path('account/get', AccountList.as_view()),
    path('account/<str:pk>', AccountDetail.as_view(), name='retrieve-account'),
    path('account/update/<str:pk>', AccountUpdate.as_view(), name='update-account'),
    path('account/delete/<str:pk>', AccountDelete.as_view(), name='delete-account'),
]
