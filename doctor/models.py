from django.db import models

# Create your models here.
class Userdata(models.Model):
    id = models.AutoField
    fname = models.CharField(max_length=500)
    lname = models.CharField(max_length=500)
    username = models.CharField(max_length=50)
    user_u_no = models.CharField(max_length=100, default="")
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=60, default="")
    address = models.TextField()


    def __str__(self):
            return self.fname

class Sessiondata(models.Model):
    username = models.CharField(max_length=500)
    join_link = models.CharField(max_length=5000)

class Doctor(models.Model):
    host_link = models.CharField(max_length=600)

class Image(models.Model):
    title = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name