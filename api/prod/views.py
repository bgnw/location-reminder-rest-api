from django.shortcuts import render
from rest_framework.response import Response

from .models import Account, TaskList, TaskItem, ItemOpportunity
from .serializers import AccountSerializer, TaskListSerializer, TaskItemSerializer, ItemOpportunitySerializer
from rest_framework import generics
from rest_framework import filters

class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountCheck(generics.ListAPIView):
    serializer_class = AccountSerializer

    def list(self, request, *args, **kwargs):
        specified_user = self.kwargs.get('username')
        specified_pass = self.kwargs.get('password')
        queryset = Account.objects.filter(username=specified_user, password=specified_pass)
        authentication_success = queryset.exists()
        return Response({"authentication_success": authentication_success})

class AccountDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountUpdate(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDelete(generics.RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TaskListCreate(generics.CreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListList(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListSearchOwner(generics.ListAPIView):
    def get_queryset(self):
        specified_owner = self.kwargs.get('username')
        return TaskList.objects.filter(owner=specified_owner)

    serializer_class = TaskListSerializer

class TaskListDetail(generics.RetrieveAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListUpdate(generics.RetrieveUpdateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListDelete(generics.RetrieveDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskItemCreate(generics.CreateAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


class TaskItemList(generics.ListAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


class TaskItemSearchListID(generics.ListAPIView):
    def get_queryset(self):
        specified_list = self.kwargs.get('list_id')
        return TaskItem.objects.filter(list=specified_list)
    serializer_class = TaskItemSerializer


class TaskItemSearchOwner(generics.ListAPIView):
    def get_queryset(self):
        specified_owner = self.kwargs.get('username')
        return TaskItem.objects.filter(owner=specified_owner)

    serializer_class = TaskItemSerializer


class TaskItemDetail(generics.RetrieveAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


class TaskItemUpdate(generics.RetrieveUpdateAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


class TaskItemDelete(generics.RetrieveDestroyAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


class ItemOpportunityList(generics.ListAPIView):
    queryset = ItemOpportunity.objects.all()
    serializer_class = ItemOpportunitySerializer

class ItemOpportunityLookup(generics.ListAPIView):
    serializer_class = ItemOpportunitySerializer
    def get_queryset(self):
        specified_item = self.kwargs.get('item_id')
        return ItemOpportunity.objects.filter(item=specified_item)


class ItemOpportunityCreate(generics.CreateAPIView):
    queryset = ItemOpportunity.objects.all()
    serializer_class = ItemOpportunitySerializer

