from django.conf import settings
from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    som = models.CharField(max_length=80)
    # usd = models.CharField(max_length=80, som * 0.012)
    # eur = models.CharField(max_length=80, som * 0.0099)
    # rub = models.CharField(max_length=80, som * 0.86)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

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
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'