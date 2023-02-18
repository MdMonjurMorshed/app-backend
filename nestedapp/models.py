

from distutils.command.upload import upload

from django.db import models
from django.utils import timezone
from datetime import datetime,date
from taggit.managers import TaggableManager


class Physics (models.Model):
    title=models.CharField(max_length=50)
    add_to_api=models.BooleanField(default=True)
    def __str__(self) :
        return self.title







class Category(models.Model):
    Category_name=models.CharField( max_length=100,blank=False)
    parent= models.OneToOneField('self',blank=True,null=True,on_delete=models.CASCADE,related_name="cat_sub")
    display_name=models.CharField(max_length=100,blank=True)
    category_image=models.ImageField(upload_to='newfile/',blank=True)
    order=models.IntegerField(blank=True,null=True)
    publish=models.BooleanField(default=True)
    has_session=models.BooleanField(default=False)
    is_sub=models.BooleanField(default=False)
    dateCreate=models.DateTimeField(default=timezone.now)  
    dateUpdate=models.DateTimeField(auto_now=True) 


    

    def __str__(self):
        
        return self.Category_name
       
       
class Depertment(models.Model):
    category=models.ForeignKey(Category,blank=False, on_delete=models.CASCADE,)
    depName=models.CharField(blank=False,max_length=100)
    shortName=models.CharField(blank=True, max_length=100)
    dep_icon=models.ImageField(blank=True,upload_to='icon/')
    dep_thumbnail=models.ImageField(blank=True, upload_to='thumbnail/')
    publish=models.BooleanField(default=True)
    depMakeDate=models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.depName


class Semester(models.Model):

    level=models.IntegerField(blank=False,null=True)
    
    startDate=models.DateField()
    endDate=models.DateField(blank=False)

    is_active=models.BooleanField(default=False)

    def __str__(self):
        return  "year "+ str(self.startDate).split('-')[0] +" semester "+str(self.level)
  
    def active_status(self):
        now=datetime.today()
        start=datetime.strptime(self.startDate, '%Y-%m-%d')
        deffer=start-now
        if(start <= now <= datetime.strptime(self.endDate, '%Y-%m-%d')):
            self.is_active=True  
        elif (self.level==1 and start.year==now.year and( start >= now) and (deffer.days<180 or deffer.days==0)) and now <= datetime.strptime(self.endDate, '%Y-%m-%d'):
            self.is_active=True
          
        else:
            self.is_active=False
    def save(self,*args, **kwargs):
        self.active_status()
        super().save(*args, **kwargs)            
        
                
        
        
class Subject(models.Model):
    name=models.CharField(max_length=100,blank=False)
    category=models.ForeignKey(Category,blank=False,on_delete=models.CASCADE)
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
    
    
############## SESSION MODEL ##############
class SessionModel(models.Model):
    name=models.CharField(max_length=50,blank=False)
    year=models.IntegerField(max_length=50,blank=False)
    publish=models.BooleanField(default=True) 
    
    def __str__(self):
        return self.name
    
class SessionCategory(models.Model):
    session=models.ForeignKey(SessionModel,on_delete=models.CASCADE,blank=True,related_name='session')
    category=models.ForeignKey(Category,blank=False,on_delete=models.CASCADE,related_name="session_category") 
    total_semester=models.IntegerField()
    is_active=models.BooleanField(default=True)
    semester=models.ManyToManyField(Semester)
    
    def __str__(self):
        return self.category.Category_name
       
     
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
    name=models.ForeignKey(Package,on_delete=models.CASCADE,blank=False,related_name="video")
    videos=models.ForeignKey(Video,on_delete=models.CASCADE,blank=False,related_name='videos')
    basic=models.BooleanField(default=False)
    premium=models.BooleanField(default=False)
    diamond=models.BooleanField(default=True)
    active=models.BooleanField(default=True)
    order=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.name.chapter.name
class Instructor (models.Model):
    name=models.CharField(max_length=50,blank=False)
    department=models.ForeignKey(Depertment,blank=False,on_delete=models.CASCADE,related_name="inst_department")
    organization=models.CharField(max_length=100,blank=False)
    picture=models.ImageField(blank=True,upload_to="instructor_pic/")  
    available=models.BooleanField(default=True)  
    creating_date=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
class CourseModel (models.Model):
    name=models.CharField(max_length=100,blank=False)
    category=models.ForeignKey(Category,blank=False,on_delete=models.CASCADE,related_name='category')
    department=models.ForeignKey(Depertment,blank=False,on_delete=models.CASCADE,related_name='department')
    subject=models.ManyToManyField(Subject,blank=False,related_name='subject')
    instructor=models.ForeignKey(Instructor,blank=True,null=True,on_delete=models.CASCADE,related_name="instructor")
    mentor=models.ForeignKey(Instructor,blank=True,null=True,on_delete=models.CASCADE,related_name="mentor")
    email=models.EmailField(blank=True,max_length=50)
    prerequisites=models.OneToOneField('self',blank=True,null=True,on_delete=models.CASCADE)
    order=models.IntegerField(blank=True,null=True)
    description=models.TextField(max_length=100,blank=False)
    facebook=models.CharField(max_length=100,blank=True)
    masenger=models.CharField(max_length=100,blank=True)
    courseIcon=models.ImageField(blank=True,upload_to='courseIcon/')
    courseBanner=models.ImageField(blank=True,upload_to='courseBanner/')
    publish= models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
        