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
        fields = '__all__'


class TaskItemSerializer(serializers.ModelSerializer):
    list = TaskListSerializer
    poi_filters2 = PoiFilterSerializer(many=True, required=False)
    class Meta:
        model = TaskItem
        fields = [
            "list",
            "owner",
            "title",
            "body_text",
            "remind_method",
            "poi_filters2",
            "attachment_img_path",
            "is_sub_task",
            "parent_task",
            "completed",
            "snooze_until",
            "due_at",
        ]

        def create(self, data):
            poi_filters_data = data.pop("poi_filters", [])
            task_item = TaskItem.objects.create(**data)
            for poi_filter_data in poi_filters_data:
                PoiFilter.objects.create(taskItem=task_item, filter=poi_filter_data)
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

