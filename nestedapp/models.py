

from distutils.command.upload import upload

from django.db import models
from django.utils import timezone
from datetime import datetime
from taggit.managers import TaggableManager


class Physics (models.Model):
    title=models.CharField(max_length=50)
    add_to_api=models.BooleanField(default=True)
    def __str__(self) :
        return self.title







class Category(models.Model):
    Category_name=models.CharField( max_length=100,blank=False)
    parent= models.OneToOneField('self',blank=True,null=True,on_delete=models.CASCADE)
    display_name=models.CharField(max_length=100,blank=True)
    category_image=models.ImageField(upload_to='newfile/',blank=True)
    order=models.IntegerField(blank=True,null=True)
    publish=models.BooleanField(default=True)
    dateCreate=models.DateTimeField(default=timezone.now)  
    dateUpdate=models.DateTimeField(auto_now=True) 


    

    def __str__(self):
        
        return self.Category_name
       
       
class Depertment(models.Model):
    category=models.ForeignKey(Category,blank=False, on_delete=models.CASCADE,related_name="category")
    depName=models.CharField(blank=False,max_length=100)
    shortName=models.CharField(blank=True, max_length=100)
    dep_icon=models.ImageField(blank=True,upload_to='icon/')
    dep_thumbnail=models.ImageField(blank=True, upload_to='thumbnail/')
    publish=models.BooleanField(default=True)
    depMakeDate=models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.depName


class Semester(models.Model):

    name=models.CharField(max_length=100,blank=False)
    category=models.ForeignKey(Category,blank= False, on_delete=models.CASCADE,related_name="category")
    department=models.ForeignKey(Depertment,blank=False,on_delete=models.CASCADE,related_name="department")
    startDate=models.DateField(default=datetime.now)
    endDate=models.DateField(blank=False)
    icon=models.ImageField(blank=True,upload_to='iconSemester/')
    publish=models.BooleanField(default=True)

    def _str__(self):
        return self.name 
class Subject(models.Model):
    name=models.CharField(max_length=100,blank=False)
    category=models.ForeignKey(Category,blank=False,on_delete=models.CASCADE,related_name="category")
    subCode=models.IntegerField(blank=False,null=True)
    order=models.IntegerField(blank=False,null=True)
    subImage=models.ImageField(blank=True,upload_to="subImage/")
    publish=models.BooleanField(default=True)
    primaryColor=models.CharField(max_length=50,blank=True)
    secondaryColor=models.CharField(max_length=50,blank=True)
    createDate=models.DateField(default=datetime.now)
    updatedDate=models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    name=models.CharField(max_length=100,blank=False)
    category=models.ForeignKey(Category,blank=False,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,blank=False,on_delete=models.CASCADE)
    publish=models.BooleanField(default=True)
    createDate=models.DateField(auto_now_add=True)   

    def __str__(self):
        return self.name
# PACKAGE MODEL
class Package(models.Model):
    category=models.ForeignKey(Category,blank=False,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,blank=False,on_delete=models.CASCADE)
    chapter=models.ForeignKey(Chapter,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.chapter.name
    

# VIDEO MODEL
class Video(models.Model):
    name=models.CharField(max_length=250,blank=False)
    tags=TaggableManager()
    url=models.CharField(max_length=250,blank=False)
    order=models.IntegerField(blank=True,null=True)
    duration=models.DecimalField(max_digits=10,blank=True,decimal_places=2,default=0.0)
    description=models.CharField(max_length=500,blank=False)
    publish=models.BooleanField(default=True)
    view=models.BooleanField(default=False)
    stream=models.BooleanField(default=False)
    thumbnail=models.ImageField(blank=True,upload_to="vid_thumb/")
    video=models.FileField(upload_to='videos/',blank=True)
    creatDate=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# VIDEO TOTIC

class videoTopic(models.Model):
    name=models.ForeignKey(Package,on_delete=models.CASCADE,blank=False,related_name="name")
    videos=models.ForeignKey(Video,on_delete=models.CASCADE,blank=False,related_name='videos')
    basic=models.BooleanField(default=False)
    premium=models.BooleanField(default=False)
    diamond=models.BooleanField(default=True)
    active=models.BooleanField(default=True)
    order=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.name.chapter.name