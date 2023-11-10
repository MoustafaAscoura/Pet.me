from django.db import models
from accounts.models import User

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()

class Photo(models.Model):
    photo = models.ImageField(upload_to="posts/images/%Y/%m/%d/%H/%M/%S/")
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='photos')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username}' 

class Report(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reports")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="reports", null=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)