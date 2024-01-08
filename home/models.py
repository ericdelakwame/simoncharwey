from django.db import models
from django.urls import reverse
from accounts.models import User
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField



class PostImage(models.Model):
    image= models.ImageField(upload_to='post/images/%Y/%m/%d', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post Image'
        verbose_name_plural = 'Post  Images'
        
    def __str__(self):
        return 'Post image uploaded on {}'.format(str(self.created))

class PostVideo(models.Model):
    video = EmbedVideoField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post Video'
        verbose_name_plural = 'Post Videos'
        
    def __str__(self):
        return 'Post video uploaded on {}'.format(str(self.created))

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100, default='')
    banner = models.ImageField(upload_to='home/posts/%Y/%m/%d', null=True, blank=True)
    description = models.TextField()
    tags = TaggableManager()
    video = EmbedVideoField(null=True, blank=True)
    videos = models.ManyToManyField(PostVideo, related_name='post_videos')
    images = models.ManyToManyField(PostImage, related_name='post_images')
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("home:post_detail", kwargs={"pk": self.pk})



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    message = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        return self.message
    