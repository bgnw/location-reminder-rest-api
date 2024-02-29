from django.db import models


class Account(models.Model):
    username = models.CharField("username", max_length=30, primary_key=True)
    display_name = models.CharField("display_name", max_length=80)
    password = models.CharField("password", max_length=200)
    biography = models.CharField("biography", max_length=600, default=None)
    profile_img_path = models.CharField("profile_img_path", max_length=1024)


class TaskList(models.Model):
    list_id = models.AutoField("list_id", primary_key=True)
    title = models.CharField("title", max_length=80)
    created_at = models.DateTimeField("created_at", default=None)
    icon_name = models.CharField("icon_name", max_length=100, default=None)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    sort_by = models.CharField("sort_by", max_length=30)
    visibility = models.PositiveSmallIntegerField("visibility", default=0)


class TaskItem(models.Model):
    item_id = models.AutoField("item_id", primary_key=True)
    body_text = models.CharField("body_text", max_length=1500, default=None)
    remind_method = models.CharField("remind_method", max_length=30, null=True)
    attachment_img_path = models.CharField("attachment_img_path", max_length=1024, default=None, null=True)
    snooze_until = models.DateTimeField("snooze_until", default=None, null=True)
    completed = models.BooleanField("completed", default=False)
    due_at = models.DateTimeField("due_at", null=True)
    is_sub_task = models.BooleanField("is_sub_task", default=False)
    parent_task = models.ForeignKey("self", on_delete=models.CASCADE, default=None, null=True)  # FK of another TaskItem


class CollaboratorPendingRequest(models.Model):
    request_id = models.AutoField("request_id", primary_key=True)
    user_sender = models.ForeignKey(Account, related_name="user_sender", on_delete=models.CASCADE)
    user_recipient = models.ForeignKey(Account, related_name="user_recipient", on_delete=models.CASCADE)
    datetime_sent = models.DateTimeField("datetime_sent", default=None)


class Collaborator(models.Model):
    collab_id = models.AutoField("collab_id", primary_key=True)
    user_master = models.ForeignKey(Account, related_name="user_master", on_delete=models.CASCADE)
    user_peer = models.ForeignKey(Account, related_name="user_peer", on_delete=models.CASCADE)


class Blocked(models.Model):
    block_id = models.AutoField("block_id", primary_key=True)
    user_blocker = models.ForeignKey(Account, related_name="user_blocker", on_delete=models.CASCADE)
    user_blockee = models.ForeignKey(Account, related_name="user_blockee", on_delete=models.CASCADE)


class ListSharedWith(models.Model):
    share_id = models.AutoField("share_id", primary_key=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    user_shared_with = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    
class TaskReminder(models.Model):
    reminder_id = models.AutoField("reminder_id", primary_key=True)
    task_item = models.ForeignKey(TaskItem, on_delete=models.CASCADE)
    reminder_type = models.CharField("reminder_type", max_length=30)
    reminder_datetime = models.DateTimeField("reminder_datetime", default=None)
    # location_category
    # business_descriptor
    # boundary
    # peer_username

