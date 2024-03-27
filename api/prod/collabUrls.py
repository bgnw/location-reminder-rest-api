from django.urls import include, path
from .views import *

urlpatterns = [
    path('rq/add/', CollabRqAdd.as_view(), name='collab-rq-add'),
    path('rq/delete/<str:pk>', CollabRqDelete.as_view(), name='collab-rq-delete'),
    path('rq/get-sent/<str:user_sender>', CollabRqSentForUser.as_view(), name='collab-rq-sent-for-user'),
    path('rq/get-received/<str:user_recipient>', CollabRqReceivedForUser.as_view(), name='collab-rq-recv-for-user'),
    path('rq/get', CollabRqList.as_view()),

    path('add/', CollaboratorAdd.as_view(), name='collab-add'),
    path('delete/<str:pk>', CollaboratorDelete.as_view(), name='collab-delete'),
    path('get-user/<str:user>', CollaboratorsForUser.as_view(), name='collab-get-for-user'),
    path('get', CollaboratorList.as_view()),
]
