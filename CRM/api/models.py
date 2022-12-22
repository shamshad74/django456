from django.db import models

# Create your models here.

class Courses(models.Model):
    course_name=models.CharField(max_length=250,unique=True)
    fees=models.PositiveIntegerField()
    duration=models.CharField(max_length=250)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class Batches(models.Model):
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    batch_code=models.CharField(max_length=200,unique=True)
    started_date=models.DateField(null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.batch_code

class Students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField(null=True)
    profile_pic=models.ImageField