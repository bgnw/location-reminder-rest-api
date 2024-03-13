from rest_framework import serializers
from .models import Account, TaskList, TaskItem, ItemOpportunity


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'


class TaskItemSerializer(serializers.ModelSerializer):
    list = TaskListSerializer
    class Meta:
        model = TaskItem
        fields = '__all__'

# class TaskItemMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaskItem
#         fields = ['item_id', 'list', 'owner', 'remind_method', 'attachment_img_path', 'snooze_until', 'completed',
#                   'due_at']


class ItemOpportunitySerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=TaskItem.objects.all()) # TaskItemSerializer()
    class Meta:
        model = ItemOpportunity
        fields = '__all__'


