from django.db import models
from accounts.models import User

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", default=1)
    content = models.TextField()
    
    def __str__(self):
        return f'{self.user.username}' 

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        # return f'{self.user.username} - {self.post.title}' 
        return f'{self.user.username}' 

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username}' 

class Photo(models.Model):
    photo = models.ImageField(upload_to="projects/images/%Y/%m/%d/%H/%M/%S/", null=True, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.name

class Report(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reports")
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="reports")
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}' 