from django.db import models
from accounts.models import User

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


# for chats between owner & adopter
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)



class Photo(models.Model):
    photo = models.ImageField(upload_to="projects/images/%Y/%m/%d/%H/%M/%S/", null=True, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='photos')



class Report(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reports")
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comments")
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
