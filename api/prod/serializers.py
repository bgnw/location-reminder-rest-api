from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'

class PoiFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoiFilter
        fields = ["filter"]


class TaskItemSerializer(serializers.ModelSerializer):
    list = TaskListSerializer
    filters = PoiFilterSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = TaskItem
        fields = [
            "item_id",
            "list",
            "owner",
            "title",
            "body_text",
            "remind_method",
            "attachment_img_path",
            "is_sub_task",
            "parent_task",
            "completed",
            "snooze_until",
            "due_at",
            "filters",
        ]

    def create(self, validated_data):
        print("in create")
        poi_filters_data = validated_data.pop("filters", [])
        task_item = TaskItem.objects.create(**validated_data)
        for poi_filter_data in poi_filters_data:
            print("in loop")
            PoiFilter.objects.create(item=task_item, **poi_filter_data)
        return task_item

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