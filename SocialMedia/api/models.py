from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images",null=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name="likes")

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
