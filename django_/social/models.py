from django.db import models
# from accounts.models import User

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()

class Photo(models.Model):
    photo = models.ImageField(upload_to="projects/images/%Y/%m/%d/%H/%M/%S/", null=True, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='photos')

class Report(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reports")
    created_at = models.DateTimeField(auto_now_add=True)
