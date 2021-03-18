from django.conf import settings
from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='picture', null=True, blank=True)
    info = models.TextField()
    money = models.CharField(max_length=80)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Gaming'

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, 
                                        related_name='comments')
    author = models.CharField(max_length=50)
    message = models.TextField()
    sent_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post_comment}"


    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Commenting'