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
    icon_name = models.CharField("icon_name", max_length=100, default=None)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    sort_by = models.CharField("sort_by", max_length=30)
    visibility = models.PositiveSmallIntegerField("visibility", default=0)


class TaskItem(models.Model):
    item_id = models.AutoField("item_id", primary_key=True)
    body_text = models.CharField("body_text", max_length=1500, default=None)
    remind_method = models.CharField("remind_method", max_length=30)
    attachment_img_path = models.CharField("attachment_img_path", max_length=1024, default=None)
    snooze_until = models.DateTimeField("snooze_until", default=None)
    completed = models.BooleanField("completed", default=False)
    due_at = models.DateTimeField("due_at")
    is_sub_task = models.BooleanField("is_sub_task", default=False)
    parent_task = models.ForeignKey("self", on_delete=models.CASCADE, default=None)  # FK of another TaskItem


class CollaboratorPendingRequest(models.Model):
    user_sender = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_recipient = models.ForeignKey(Account, on_delete=models.CASCADE)
    datetime_sent = models.DateTimeField("datetime_sent", default=None)


class Collaborator(models.Model):
    user_master = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_peer = models.ForeignKey(Account, on_delete=models.CASCADE)


class Blocked(models.Model):
    user_blocker = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_blockee = models.ForeignKey(Account, on_delete=models.CASCADE)


class ListSharedWith(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    
    
class TaskReminder(models.Model):
    task_item = models.ForeignKey(TaskItem, on_delete=models.CASCADE)
    reminder_type = models.CharField("reminder_type", max_length=30)
    reminder_datetime = models.DateTimeField("reminder_datetime", default=None)
    # location_category
    # business_descriptor
    # boundary
    # peer_username

