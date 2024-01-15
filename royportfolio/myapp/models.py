from django.db import models

# Create your models here.
# Starting og Blog Section 
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    thumbleimage =  models.ImageField(upload_to ='thumbleimg')  # pic must be 600x400

    blogimg1 = models.ImageField(upload_to ='blogpic1',blank=True,null=True)  
    content1 = models.TextField(blank=True)
    blogimg2 = models.ImageField(upload_to ='blogpic1',blank=True,null=True)  
    content2 = models.TextField(blank=True)
    blogimg3 = models.ImageField(upload_to ='blogpic1',blank=True,null=True)  
    content3 = models.TextField(blank=True)
    blogimg4 = models.ImageField(upload_to ='blogpic1',blank=True,null=True)  
    content4 = models.TextField(blank=True)
    blogimg5 = models.ImageField(upload_to ='blogpic1',blank=True,null=True)  
    content5 = models.TextField(blank=True)
    blogimg6 = models.ImageField(upload_to ='blogpic1',blank=True,null=True)  
    content6 = models.TextField(blank=True)
    blogimg7 = models.ImageField(upload_to ='blogpic1',blank=True,null=True)  
    content7 = models.TextField(blank=True)
    blogimg8 = models.ImageField(upload_to ='blogpic1',blank=True,null=True)  
    content8 = models.TextField(blank=True)
    
    productname = models.CharField(max_length=50,blank=True)
    link = models.CharField(max_length=255,blank=True)
    timeStamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=130)
    
    def __str__(self):
        return self.title




class Contact(models.Model):
    email = models.CharField(max_length=100)

class Homeimg(models.Model):
    homeimage = models.ImageField(upload_to ='home1',blank=True,null=True) 
    blogtop =  models.ImageField(upload_to ='home1',blank=True,null=True) 