from django.db import models
from django.contrib.auth.models import User,auth
class contact(models.Model):
    site_owner = models.OneToOneField(User, on_delete=models.CASCADE, )
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField()
    resume=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    file=models.FileField(upload_to='files/%Y/%m/%d/',blank=True,null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

        
