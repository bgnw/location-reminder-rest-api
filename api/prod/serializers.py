import json
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

class PoiFilterOnlyFilterFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoiFilter
        fields = ["filters"]


class TaskItemSerializer(serializers.ModelSerializer):
    list = TaskListSerializer
    filters = PoiFilterOnlyFilterFieldSerializer(many=True, required=True)
    applicable_filters = serializers.SerializerMethodField()
    class Meta:
        model = TaskItem
        fields = [
            "item_id",
            "list",
            "owner",
            "title",
            "body_text",
            "remind_method",
            "user_peer",
            "attachment_img_path",
            "is_sub_task",
            "parent_task",
            "completed",
            "snooze_until",
            "due_at",
            "lati",
            "longi",
            "filters",
            "applicable_filters"
        ]

    def get_applicable_filters(self, obj):
        filters_for_item = PoiFilter.objects.filter(item=obj.item_id)
        serializer = PoiFilterSerializer(filters_for_item, many=True)
        return serializer.data

    def create(self, validated_data):
        poi_filters_data = validated_data.pop("filters", [])
        task_item = TaskItem.objects.create(**validated_data)
        for poi_filter_data in poi_filters_data:
            print("in loop")
            PoiFilter.objects.create(item=task_item, **poi_filter_data)
        return task_item


class ItemOpportunitySerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=TaskItem.objects.all()) # TaskItemSerializer()
    class Meta:
        model = ItemOpportunity
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class CollaboratorPendingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaboratorPendingRequest
        fields = '__all__'


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'