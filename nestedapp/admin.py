from django.contrib import admin
from .models import  Physics, Category,Depertment,Semester,Subject,Chapter,Video,Package,videoTopic,Instructor,CourseModel,SessionModel,SessionCategory


@admin.register(Physics)
class PhysicsAdmin(admin.ModelAdmin):
    list_display=['id']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","order","Category_name","display_name","parent","category_image","publish")

@admin.register(Depertment)
class DepertmentAdmin(admin.ModelAdmin):
    list_display=("id","category","depName","shortName","dep_icon","dep_thumbnail","publish")
    

admin.site.register(Semester)


@admin.register(Subject)
class SubAdmin(admin.ModelAdmin):
    list_display=("id","name","category","subCode","subImage","primaryColor","secondaryColor","publish")    
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display=("id","name","category","createDate","publish")   

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display=("id","name")        

@admin.register(Package)
class packageAdmin(admin.ModelAdmin):
    list_display=['id','chapter']

@admin.register(videoTopic)
class topicAdmin(admin.ModelAdmin):
    list_display=['id','name']


@admin.register(Instructor)
class InsAdmin(admin.ModelAdmin):
    list_display=["id","name"]
    
@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display=["id","name","category","department"]    
    
@admin.register(SessionModel)
class SessionAdmin(admin.ModelAdmin):
    list_display=['id','name','year','publish']     
    
@admin.register(SessionCategory)
class SesscionCatAdmin(admin.ModelAdmin):
    list_display=['id','category','session']       

 
           