from rest_framework import serializers
from .models import Account, TaskList, TaskItem


class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['username','display_name','password','biography','profile_img_path']


class TaskListSerializer(serializers.ModelSerializer):
	remind_method = serializers.CharField("remind_method", max_length=30, required = False, allow_null = True)
	attachment_img_path = serializers.CharField("attachment_img_path", max_length=1024, default=None, required = False, allow_null = True)
	snooze_until = serializers.DateTimeField("snooze_until", default=None, required = False, allow_null = True)
	completed = serializers.BooleanField("completed", default=False, required = False, allow_null = True)
	due_at = serializers.DateTimeField("due_at", default=None, required = False, allow_null = True)
	is_sub_task = serializers.BooleanField("is_sub_task", default=False, required = False, allow_null = True)
	parent_task = serializers.ForeignKey("self", default=None,
									required = False, allow_null = True)  # FK of another TaskItem
	class Meta:
		model = TaskList
		fields = ['list_id','title','icon_name','created_at','owner','sort_by','visibility']


class TaskItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskItem
		fields = ['item_id','body_text','remind_method','attachment_img_path','snooze_until','completed','due_at','is_sub_task','parent_task']
