from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from sorl.thumbnail import ImageField

class Post(models.Model):
    ign = models.CharField(max_length=100, blank=True)
    uid = models.CharField(max_length=19 ,blank=True, unique=True)
    content = models.TextField(default='Reason for report...')
    image = models.FileField(blank=True, upload_to='postpics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    dislikes = models.ManyToManyField(User, related_name='blog_posts2')

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
    
    


    def __str__(self):
        return self.ign

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    






    
