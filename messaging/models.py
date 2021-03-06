from django.db import models
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from random import choice
from string import ascii_letters
from django.utils import timezone


def random_slug_gen(number=9):
    return "".join(choice(ascii_letters) for i in range(number))


class ChatingRoomObject(models.Manager):

    def get_or_create_room(self, username1, username2):
        for i in [username1, username2]:
            if type(i) != type("str"):
                raise Http404()

        user1 = get_object_or_404(User, username=username1)
        user2 = get_object_or_404(User, username=username2)

        qs1 = self.filter(user1=user1, user2=user2)
        if qs1.exists():
            return qs1.get()

        qs2 = self.filter(user2=user1, user1=user2)
        if qs2.exists():
            return qs2.get()

        obj = self.create(user1=user1, user2=user2)
        return obj

    def filter_room(self, username1, username2):
        for i in [username1, username2]:
            if type(i) != type("str"):
                raise Http404()

        user1 = get_object_or_404(User, username=username1)
        user2 = get_object_or_404(User, username=username2)

        qs1 = self.filter(user1=user1, user2=user2)
        if qs1.exists():
            return qs1.get()

        qs2 = self.filter(user2=user1, user1=user2)
        if qs2.exists():
            return qs2.get()

        return None


class ChatingRoom(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1_chating_room")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2_chating_room")

    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = ChatingRoomObject()

    class Meta:
        unique_together = ["user1", "user2"]

    def __str__(self):
        return f"{self.user1} and {self.user2} Chating-Room..."

    def get_chatted_with_user(self, user):
        if user == self.user1:
            return self.user2
        
        elif user == self.user2:
            return self.user1

        return None


class ChatingRoomMessage(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1_msgs")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2_msgs")
    message = models.TextField()
    chat_room = models.ForeignKey(ChatingRoom, on_delete=models.CASCADE, related_name="ch_messages")
    slug = models.SlugField()
    sent_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msgs_sent_by")
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_created", ]

    def save(self, *args, **kwargs):
        slug = self.slug

        if slug is None or slug == "" or slug == "slug":
            self.slug = slugify(str(self.message[:10]) + random_slug_gen(10))

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user1} and {self.user2} Messages..."


class Notifications(models.Model):
    NOTIFICATION_CATEGORY = (
        ("FR", "FRIEND_REQUEST"),
        ("VT", "VOTED_TRUE"),
        ("VF", "VOTED_FALSE"),
        ("GC", "GOSSIP_COMMENT"),
        ("CR", "COMMENT_REPLY"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_nots")    
    message = models.TextField()
    slug = models.SlugField()
    url = models.CharField(max_length=2040, blank=True, null=True)
    seen = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=2, choices=NOTIFICATION_CATEGORY, blank=True, null=True)
    data = models.JSONField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} Notifications..."

    def save(self, *args, **kwargs):
        slug = self.slug

        if slug is None or slug == "" or slug == "slug":
            self.slug = slugify(str(self.message[:10]) + random_slug_gen(9))

        return super().save(*args, **kwargs)
