from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

#customized query sets
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager,self).get_queryset()\
                .filter(status='published')

# Models for Posts
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,max_length=250,
                                on_delete=models.CASCADE,
                                related_name='blog_posts')
    slug = models.SlugField(max_length=200,
                            unique_for_date='publish')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=timezone.now)
    publish = models.DateTimeField(default = timezone.now)
    updated = models.DateTimeField(auto_now = timezone.now)
    status = models.CharField(max_length=20,
                            choices = STATUS_CHOICES,
                            default = 'publish')
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()# default Manager
    published = PublishManager()# user defined Manager

    def get_absolute_url(self):
        return reverse("User_posts:details",
                        args = [self.publish.year,
                                self.publish.month,
                                self.publish.day,self.slug])
