from django.db import models
from django.utils import timezone


class Account(models.Model):
    username = models.CharField("username", max_length=30, primary_key=True)
    display_name = models.CharField("display_name", max_length=80)
    password = models.CharField("password", max_length=200)
    biography = models.CharField("biography", max_length=600, default=None)
    profile_img_path = models.CharField("profile_img_path", max_length=1024)
    lati = models.DecimalField("lati", max_digits=12, decimal_places=9, null=True)
    longi = models.DecimalField("longi", max_digits=12, decimal_places=9, null=True)


class TaskList(models.Model):
    list_id = models.AutoField("list_id", primary_key=True)
    title = models.CharField("title", max_length=80)
    created_at = models.DateTimeField("created_at")
    icon_name = models.CharField("icon_name", max_length=100, null=True, blank=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    sort_by = models.CharField("sort_by", max_length=30)
    visibility = models.PositiveSmallIntegerField("visibility", default=0)


class TaskItem(models.Model):
    item_id = models.AutoField("item_id", primary_key=True)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    owner = models.ForeignKey(Account, related_name="owner", on_delete=models.CASCADE)
    title = models.CharField("title", max_length=100)
    body_text = models.CharField("body_text", max_length=1500, null=True, blank=True)
    remind_method = models.CharField("remind_method", max_length=30, null=True, blank=True)
    user_peer = models.ForeignKey(Account, related_name="task_user_peer", on_delete=models.CASCADE, null=True, blank=True)
    attachment_img_path = models.CharField("attachment_img_path", max_length=1024, null=True, blank=True)
    is_sub_task = models.BooleanField("is_sub_task", null=True, blank=True)
    parent_task = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)  # FK of another TaskItem
    completed = models.BooleanField("completed", default=False)
    snooze_until = models.DateTimeField("snooze_until", null=True, blank=True)
    due_at = models.DateTimeField("due_at", null=True, blank=True)
    lati = models.DecimalField("lati", max_digits=12, decimal_places=9, null=True, blank=True)
    longi = models.DecimalField("longi", max_digits=12, decimal_places=9, null=True, blank=True)
    filters = models.CharField("filters", max_length=1, null=True, blank=True)

class PoiFilter(models.Model):
    entry_id = models.AutoField("entry_id", primary_key=True)
    item = models.ForeignKey(TaskItem, on_delete=models.CASCADE)
    filters = models.CharField("filter", max_length=100)


class ItemOpportunity(models.Model):
    opp_id = models.AutoField("opp_id", primary_key=True)
    item = models.ForeignKey(TaskItem, on_delete=models.CASCADE)
    suppressed = models.BooleanField("suppressed", default=False)
    place_name = models.CharField("place_name", max_length=200)
    category = models.CharField("category", max_length=200)
    lati = models.DecimalField("lati", max_digits=12, decimal_places=9)
    longi = models.DecimalField("longi", max_digits=12, decimal_places=9)
    alti = models.DecimalField("alti", max_digits=12, decimal_places=9)


class CollaboratorPendingRequest(models.Model):
    request_id = models.AutoField("request_id", primary_key=True)
    user_sender = models.ForeignKey(Account, related_name="user_sender", on_delete=models.CASCADE)
    user_recipient = models.ForeignKey(Account, related_name="user_recipient", on_delete=models.CASCADE)
    datetime_sent = models.DateTimeField("datetime_sent", default=timezone.now)


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


class Log(models.Model):
    entry_id = models.AutoField("entry_id", primary_key=True)
    timestamp = models.DateTimeField("timestamp", default=timezone.now)
    lati = models.DecimalField("lati", max_digits=12, decimal_places=9)
    longi = models.DecimalField("longi", max_digits=12, decimal_places=9)
    notes = models.CharField("comments", max_length=2000)
