from django.urls import include, path
from .views import *

urlpatterns = [
    path('rq/add/<str:user_sender>/<str:user_recipient>', CollabRqAdd.as_view(), name='collab-rq-add'),
    path('rq/delete/<str:user_sender>/<str:user_recipient>', CollabRqDelete.as_view(), name='collab-rq-delete'),
    path('get-sent/<str:user_master>', CollabRqSentForUser.as_view(), name='collab-rq-sent-for-user'),
    path('get-received/<str:user_master>', CollabRqReceivedForUser.as_view(), name='collab-rq-recv-for-user'),
    path('rq/get', CollabRqList.as_view()),

    path('add/<str:user_master>/<str:user_peer>', CollaboratorAdd.as_view(), name='collab-add'),
    path('delete/<str:user_master>/<str:user_peer>', CollaboratorDelete.as_view(), name='collab-delete'),
    path('get-user/<str:user_master>', CollaboratorsForUser.as_view(), name='collab-get-for-user'),
    path('get', CollaboratorList.as_view()),
]
