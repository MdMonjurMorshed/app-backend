from django.contrib import admin
from .models import  CourseModel, Instructor, Physics, Category,Depertment,Semester,Subject,Chapter,Video,Package,videoTopic


@admin.register(Physics)
class PhysicsAdmin(admin.ModelAdmin):
    list_display=['id']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","order","Category_name","display_name","parent","category_image","publish")

@admin.register(Depertment)
class DepertmentAdmin(admin.ModelAdmin):
    list_display=("id","category","depName","shortName","dep_icon","dep_thumbnail","publish")
    

@admin.register(Semester)
class SemAdmin(admin.ModelAdmin):
    list_display=("id","category","name","department","icon","startDate","endDate","publish")

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


 
           