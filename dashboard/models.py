from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Work(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("dashboard:work_detail", kwargs={"pk": self.pk})


class Teaching(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Teaching'
        verbose_name_plural = 'Teaching'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("dashboard:teaching_detail", kwargs={"pk": self.pk})


class About(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'About Entry'
        verbose_name_plural = 'About Entries'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("dashboard:about_detail", kwargs={"pk": self.pk})



class Press(models.Model):
    date = models.DateField()
    feature = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'Press'
        verbose_name_plural = 'Press Entries'
    
    def __str__(self):
        return self.feature
    
    def get_absolute_url(self):
        return reverse("dashboard:press_detail", kwargs={"pk": self.pk})
    
    