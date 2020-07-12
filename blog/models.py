from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Blogs(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blog_heading=models.CharField(max_length=50)
    blog_text=models.CharField(max_length=50)

    def __str__(self):
        return self.blog_heading