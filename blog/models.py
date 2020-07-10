from django.db import models
from accounts.models import User

# Create your models here.
class BlogPost(models.Model):
    POST_CATEGORY = (
        ('Education','Education'),
        ('Tech','Tech'),
        ('Automobile','Automobile'),
        ('Other','Other')
    )
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='Blog Thumbnail')
    category = models.CharField(max_length=100, choices = POST_CATEGORY )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    tags = models.CharField(max_length=150, null=True, blank=True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    
    def __str__(self):
        return self.title
    
      

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.email+"---"+self.message
    
    
    
class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment