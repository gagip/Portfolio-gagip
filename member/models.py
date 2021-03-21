from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    introduce = models.TextField(blank=True)
    picture = models.ImageField(upload_to='picture', default='picture/no-img.jpg')