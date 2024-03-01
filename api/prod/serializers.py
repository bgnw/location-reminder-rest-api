from rest_framework import serializers
from .models import Account, TaskList, TaskItem


class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['username','display_name','password','biography','profile_img_path']


class TaskListSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskList
		fields = ['list_id','title','icon_name','created_at','owner','sort_by','visibility']


class TaskItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskItem
		fields = ['item_id', 'list', 'owner', 'body_text','remind_method','attachment_img_path','snooze_until','completed','due_at','is_sub_task','parent_task']
