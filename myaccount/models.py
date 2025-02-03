from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 

class MyAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
