from django.db import models

# Create your models here.
class Student(models.Model):
    # student_id=models.CharField(max_length=20)
    # name=models.TextField()
    # address=models.TextField()
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.TextField()
    class Meta:
        verbose_name_plural="Student_details"
    def __str__(self):
        return self.name+self.address

class Registration(models.Model):
    reg_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    # address = models.TextField()
    # # country = models.TextField()
    # gender = models.TextField()
    username = models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name + self.lastname+self.address+self.username+self.password

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    photo = models.FileField(upload_to="images/")
    class Meta:
        verbose_name_plural="User"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255,default='',blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title