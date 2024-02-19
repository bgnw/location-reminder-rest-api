from django.shortcuts import render
from .models import Account, TaskList, TaskItem
from .serializers import AccountSerializer, TaskListSerializer, TaskItemSerializer
from rest_framework import generics

class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


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


class TaskListDetail(generics.RetrieveAPIView):
    queryset = TaskList.objects.all()
    serializer_class = AccountSerializer


class TaskListUpdate(generics.RetrieveUpdateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = AccountSerializer


class TaskListDelete(generics.RetrieveDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = AccountSerializer


class TaskItemCreate(generics.CreateAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


class TaskItemList(generics.ListAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


class TaskItemDetail(generics.RetrieveAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = AccountSerializer


class TaskItemUpdate(generics.RetrieveUpdateAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = AccountSerializer


class TaskItemDelete(generics.RetrieveDestroyAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = AccountSerializer
