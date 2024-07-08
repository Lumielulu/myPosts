from django.db import models as m
from django.contrib.auth.models import User

# Create your models here.

class userProfile(m.Model):
    user = m.OneToOneField(User, on_delete=m.CASCADE)
    user_pic = m.ImageField(blank=True, null=True)
    user_bio = m.TextField(default='')



class userPost(m.Model):
    id = m.AutoField(primary_key=True)
    user = m.ForeignKey(User, on_delete=m.CASCADE, related_name='posts')
    post_pic = m.ImageField(blank=True, null=True)
    content = m.TextField()
    created_at = m.DateTimeField(auto_now_add=True)
