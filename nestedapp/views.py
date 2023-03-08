from urllib import response
from django.contrib import messages
from multiprocessing import context
from django.forms import model_to_dict

from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import request
from django.contrib.auth.models import User
from .form import ParentForm ,DepForm,SubForm,ChapterForm,VidForm,PackForm,CourseForm,instForm,SessionForm,EndwiseCourseForm
from .filter import filterModel, DepFilter,SubFilter,ChapFilter,VidFilter,instFilter
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType

from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from .models import Category, Physics,Depertment,Semester,Subject,Chapter,Video,Package,videoTopic,Instructor,CourseModel,SessionModel,SessionCategory
from .serializers import TopicSerializer,PackageSerialize,VideoSerialize,CatSerializer,DepertSerializer,SemesterSerializer,SubSerializer,ChapSerializer,CourseSerialize,InstSerialize,SessionCatSerial,SessionSerial
from django.contrib.auth import authenticate,login,logout
from taggit.models import TaggedItem
import json
from rest_framework import serializers



def FrontView(request): 
    return render(request,'nestedapp/base.html',{})  
def Dashboard(request):
    if request.user.is_authenticated:
        
       return render(request,'nestedapp/base.html',{})     
    else:
        return redirect("login")
def loginview(request):
    
    
    if request.user.is_authenticated:
            return redirect('dash')

            

        
    if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username,password)
            user=authenticate(request,username=username,password=password)
            if user is None:
                context={
                    "error":"something happend"
                }

           
                return render(request,'nestedapp/login.html',context)
            login(request,user)
            return redirect('dash')
    return render(request,"nestedapp/login.html")

def LogoutView(request):
    if request.method== 'POST':
        logout(request)
        redirect('login')
        
        

    return render(request,'nestedapp/logout.html')
   
          
def CreateCategory(request):
    if request.user.is_authenticated:
        if request.method == "POST":
           

           fm=ParentForm(request.POST,request.FILES)
           

           if fm.is_valid():
              
               fm.save()
           
               messages.success(request,"data is added successfully")
               return redirect('category')

        else:
            fm=ParentForm()

       
    
        context={
       
        "form":fm

          }     
      
        
        return render(request,'nestedapp/category_page.html',context)
    return redirect('login')    

    

    


def CategoryList(request):
    obj=Category.objects.all()
    
    filter=filterModel(request.GET,queryset=obj)
    paginnator=Paginator(filter.qs,8)
    page_num=request.GET.get('page')
    page_obj=paginnator.get_page(page_num)
    nums= "a" * page_obj.paginator.num_pages
    context={
        "filter":filter,
        "c_data":page_obj,
        "nums":nums
        

    }
       
    return render(request,'nestedapp/category_list.html',context)

def CategoryUpdate(request,id):
    if request.method == "POST":
        mi= Category.objects.get(pk=id)
        fi=ParentForm(request.POST,request.FILES,instance=mi)
        if fi.is_valid:
            fi.save()
            messages.success(request,"data has been updated ")
            
    oneItem=Category.objects.get(pk=id)
    frm=ParentForm(instance=oneItem)
    return render(request,'nestedapp/category_update.html',{'frm':frm })


def CategoryDelete(request,id):
    mi=Category.objects.get(pk=id)
    if request.method=="POST":
        mi.delete()
        return redirect('catlist')

    return render(request,'nestedapp/delete.html',{"form":mi})   
        
 
 #   for department view

def CreateDep(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            frm=DepForm(request.POST,request.FILES)
            if frm.is_valid():

                frm.save()
                messages.success(request,"data is added successfully")
                return redirect('department')
      
        frm=DepForm()
        context={
            "form":frm

        }    
        return render(request,'nestedapp/depPage.html',context)
    return redirect('login')    

def DepList(request):
    dep=Depertment.objects.all()
    depfilter= DepFilter(request.GET, queryset=dep)
    paginator=Paginator(depfilter.qs,10)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    num= "a" * page_obj.paginator.num_pages

    context={
        "filter":depfilter,
        "dep_data":page_obj,
        "nums":num

    }

    return render(request,"nestedapp/depList.html",context)

def DepUpdate(request,id):
    if request.method == "POST":
        dmi=Depertment.objects.get(pk=id)
        dfi=DepForm(request.POST,request.FILES,instance=dmi)
        if dfi.is_valid():
            dfi.save()
            messages.success(request,'data is updated successfully')

    dep_obj=Depertment.objects.get(pk=id)
    form=DepForm(instance=dep_obj)

    return render(request,'nestedapp/depUpdate.html',{"form":form})    
def depDelete(request,id):
    dep_obj=Depertment.objects.get(pk=id)

    if request.method =="POST":
        dep_obj.delete()
        return redirect("dep-list")
        

    return render(request,"nestedapp/depDelete.html",{"form":dep_obj})
def depload(request):
    parent_value=request.GET.get('parent_value',None)
    dep_data=Depertment.objects.filter(category_id=parent_value).order_by('depName')


    
    return JsonResponse(list(dep_data.values('id','depName')),safe=False)    

# for Semester view


# def SemView(request):
#     if request.user.is_authenticated:
#         if request.method=="POST":
#             form=SemForm(request.POST,request.FILES)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request,"data added successfully")


#         form=SemForm()
#         context={
#         "form":form
#     }
#         return render(request,'nestedapp/semesterPage.html',context)

#     return redirect('login')

# def SemList(request):
#     sem=Semester.objects.all()
#     filter=SemFilter(request.GET,queryset=sem)
#     paginator=Paginator(filter.qs,10)
#     page_num=request.GET.get('page')
#     page_obj=paginator.get_page(page_num)
#     num="a" * page_obj.paginator.num_pages
#     context={
#         "filter":filter,
#         "page_obj":page_obj,
#         "nums":num
#     }
#     return render(request,"nestedapp/semlist.html",context)
# def semUpdate(request,id):
#     smi=Semester.objects.get(pk=id)
#     if request.method=="POST":
#         form=SemForm(request.POST,request.FILES,instance=smi)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"data is updated successfully")

#     form=SemForm(instance=smi)
#     context={
#         "form":form
#     }
#     return render(request,"nestedapp/semesterPage.html",context)
# def semDelete(request,id):
#     smi=Semester.objects.get(pk=id)
#     if request.method=="POST":
#        smi.delete()
#     context={
#         "delete":smi
#     }
#     return render(request,"nestedapp/allDelete.html", context)



# FOR SUBJECT VIEWS

def subPage(request):
    if request.user.is_authenticated:

         if request.method== "POST":
            form=SubForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"data is added successfully")
         form=SubForm()
         context={
        'form':form
              }
         return render(request,"nestedapp/subPage.html",context)
    return redirect('login')     
def SubList(request): 
    sub_mi=Subject.objects.all()
    filter=SubFilter(request.GET,queryset=sub_mi)
    paginator=Paginator(filter.qs,10)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    num= "a" * page_obj.paginator.num_pages
    context={
        'page_obj':page_obj,
        'filter':filter,
        'nums':num
    }
    return render  (request,"nestedapp/subList.html",context)

def SubUpdate(request,id):
    sub_mi=Subject.objects.get(pk=id)
    if request.method=="POST":
        form=SubForm(request.POST,request.FILES,instance=sub_mi)
        if form.is_valid():
            form.save()
            messages.success(request,"data has been updated successfully")
    form=SubForm(instance=sub_mi)
    context={
        'form':form
    }

    return render(request,"nestedapp/subPage.html",context)

def SubDelete(request,id):
    sub_mi=Subject.objects.get(pk=id)
    if request.method=="POST":
        sub_mi.delete()
    context={
        "delete":sub_mi
    }


    return render(request,'nestedapp/allDelete.html',context)

# VIEWS FOR CHAPTER

def ChapList(request):
    if request.method=="POST":
        form=ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"data is added successfully")
    form=ChapterForm()
    chap_mi=Chapter.objects.all()
    filter=ChapFilter(request.GET,queryset=chap_mi)
    paginator=Paginator(filter.qs,10)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    num="a" * page_obj.paginator.num_pages
    context={
        "form":form,
        "filter":filter,
        "page_obj":page_obj,
        "nums":num
    }
    return render( request,'nestedapp/chapterList.html',context)    

def ChapUpdate(request,id):
    chap_mi=Chapter.objects.get(pk=id)
    form=ChapterForm(instance=chap_mi)
    if request.method=="POST":
        form=ChapterForm(request.POST,instance=chap_mi)
        if form.is_valid():
            form.save()
            messages.success(request,'data is updated successfully')
        
    context={
        'form':form
    }
    return render(request,'nestedapp/chapUpdate.html',context)

def ChapDelete(request,id):
    
    chap_mi=Chapter.objects.get(pk=id)
    if request.method=="POST":
        
        chap_mi.delete()
        return redirect("chapter")

    context={
        'delete':chap_mi,
        'title':'chapter',
    }

    return render(request,'nestedapp/allDelete.html',context)        

#   VIDEO VIEW
def VidView(request):
    if request.method=="POST":
        form=VidForm(request.POST,request.FILES)
        if form.is_valid():

            form.save()
         

            
            messages.success(request,'video is uploaded successfully')
    form=VidForm()
    context={
        'form':form
    }
    return render(request,'nestedapp/uploadVideo.html',context)    


def VideoList(request):
    vid_mi=Video.objects.all()   
    filter=VidFilter(request.GET,queryset=vid_mi)
    paginator=Paginator(filter.qs,10)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    num= "a" * page_obj.paginator.num_pages
    context={
        "filter":filter,
        "page_obj":page_obj,
        "nums":num
    }
    return render(request,'nestedapp/videoList.html',context)

def VidUpdate(request,id):
    vid_mi=Video.objects.get(pk=id)
    form=VidForm(instance=vid_mi)
    if request.method=="POST":
        form=VidForm(request.POST,request.FILES,instance=vid_mi)
        if form.is_valid():
            form.save(commit=False)
            form.save_m2m()
            messages.success(request,'Update successfull')
    context={
    "form":form
    }
    return render(request,'nestedapp/uploadVideo.html',context)

def VidDelete(request,id):
    vid_mi=Video.objects.get(pk=id)
    if request.method=="POST":
        vid_mi.delete()
    context={
        'title':'vid-list',
        "delete":vid_mi
    }    
    return render(request,'nestedapp/allDelete.html',context)
def VidDetails(request,id):
    vid_mi=Video.objects.get(pk=id)

    context={
        'title':'vid-list',
        'form':vid_mi
    }
    return render(request,'nestedapp/vidDetails.html',context)


    # PACKAGE VIEW
def PackageView(request):
    category_id=request.GET.get('category')
    subject=Subject.objects.filter(category_id=category_id).order_by('name')
    form=PackForm()
    context={
        'subject':subject,
        'form':form
    }
    if request.method=="POST":
        
      category=request.POST.get('category')  
      category1=Category.objects.get(pk=category)
    
      subject=request.POST.get('subject') 
      subject1=Subject.objects.get(pk=subject) 
      chapter=request.POST.get('chapter')
      chapter1=Chapter.objects.get(pk=chapter)
      
      video=request.POST.getlist('video_ids[]')
     
      basic = request.POST.getlist('basic_videos[]')
      premium = request.POST.getlist('premium_videos[]')
      diamond = request.POST.getlist('diamond_videos[]')
      active = request.POST.getlist('active_videos[]') 

       
      order=request.POST.getlist('video_orders[]')
      print('basic list:',basic)
      print('premium list:',premium)
      for b in enumerate(basic):
          print("basic vid id:",b)
     
      package=Package(category=category1,subject=subject1,chapter=chapter1)
 
     
      package.save()
      num_videos = len(video)

      # Make sure all lists are the same length
      if len(basic) < num_videos:
          basic += [False] * (num_videos - len(basic))
      if len(premium) < num_videos:
         premium += [False] * (num_videos - len(premium))
      if len(diamond) < num_videos:
         diamond += [False] * (num_videos - len(diamond))
      if len(active) < num_videos:
         active += [False] * (num_videos - len(active))
      for i,vid in enumerate(video):
            basic_value = bool(basic[i])
            premium_value = bool(premium[i])
            diamond_value = bool(diamond[i]) 
            active_value = bool(active[i]) 
              
            print("video id:",vid)
            print("basic in index I: ",(b[i] for b in basic))
                        
            video_topic=videoTopic(name=package,videos=Video.objects.get(pk=int(vid)),basic= basic_value,premium=premium_value ,diamond=diamond_value,active=active_value,order=order[i])
            video_topic.save()
                   
                
      messages.success(request,"data is added successfully")
   
         
    return render(request,"nestedapp/package.html",context)    



def loadSubject(request):
    category_id=request.GET.get('category')
    subject=Subject.objects.filter(category_id=category_id).order_by('name')
 
    context={
        'subjects':subject,
    }
    return JsonResponse(list(subject.values('id','name')),safe=False)
    
    #return render(request,'nestedapp/subjectLoad.html',context)    

def loadChap(request):
    subject_id=request.GET.get('subject')
 
    chapter=Chapter.objects.filter(subject_id=subject_id).order_by('name')
    context={
        'chapter':chapter
    }    
    #return render(request,"nestedapp/chapterLoad.html",context)
    return JsonResponse(list(chapter.values('id','name')),safe=False)
def VidSearch(request):
  
    query=request.GET.get('q')
        
    video=Video.objects.filter(tags__name__contains=query).order_by('name').distinct()
    a=[i for i in range(len(video))]
    
    print(a)
    vi=[i.tags.names() for i in video]
  
    d=[{'id':k.id,'name':k.name,'thumbnail':''.join(str(k.thumbnail)),'tags':','.join(k.tags.names())} for k in video]
    print(d)
    print(json.dumps(list(d)))
 
    return JsonResponse(d,safe=False)
  
 # VIEW FOR VIDEO TOPICS
 
def topicView(request):
    if request.method=="POST":
      category=request.POST.get('category')  
      subject=request.POST.get('subject')  
      chapter=request.POST.get('chapter')
      package=Package(category=category,subject=subject,chapter=chapter)
      package.save()
      video=request.POST.getlist('video_ids[]')
     
     
      basic=request.POST.getlist('basic_videos[]')
      premium=request.POST.getlist('premium_videos[]')
      diamond=request.POST.getlist('diamond_videos[]')
      active=request.POST.getlist ('active_videos[]')
      for i,vid in video:
          
    
      
         video_topic=videoTopic(name=chapter,videos=vid,basic=basic,premium=premium,diamond=diamond,active=active,)
   
      video_topic.save()

# VIEW FORM THE COURSE MODEL
def CourseView(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
       
        if form.is_valid():
            
            form.save()
            messages.success(request,"course is added successfully")
        else:
            print(str(form.errors)) 
         
        
    frm=CourseForm()
     
    return render(request,'nestedapp/course.html',{'form':frm})

#  VIEW FOR INSTRUCTOR

def InstView(request):
    if request.method=="POST":
        form=instForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"data is added successfully")
            return redirect('instructor')
            
    form=instForm()
    inst_mi=Instructor.objects.all()
    filter=instFilter(request.GET,queryset=inst_mi)
    paginator=Paginator(filter.qs,10)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    num="a" * page_obj.paginator.num_pages
    context={
        "form":form,
        "filter":filter,
        "page_obj":page_obj,
        "nums":num
    }
    return render( request,'nestedapp/instructor.html',context)














####################  TEST VIEW #################

def TableView(request):
    table_data=list(Video.objects.values('name','id','creatDate','publish'))
    
    ct=ContentType.objects.get(model="video")
    new_list=[{"name":k['name'],"tags": [tag_item.tag.name for tag_item in TaggedItem.objects.filter(object_id=k["id"]).distinct()],"publish":"activated" if k["publish"]==True else"Deactivated","creatDate":k["creatDate"] ,"id":k["id"]}for k in table_data]
   
    return JsonResponse(new_list,safe=False)

def table(request):
    return render(request,"nestedapp/vido_dataTable.html")

def newDataTable(request):
    list_model=list(Video.objects.values("name","id","publish","creatDate"))
    data_list=[{"name":k['name'],"id":k['id'],"tags":[ tag_item.tag.name for tag_item in TaggedItem.objects.filter(object_id=k['id']).distinct()],"publish":"activated" if k['publish']==True else "deactivated","creatDate":k['creatDate']} for k in list_model]
    
    
    
    return JsonResponse(data_list,safe=False)
def newVidList(request):
    return render(request,"nestedapp/newVid_list.html")


def categoryAndSession(request):
    category=Category.objects.all()
    session=SessionModel.objects.all()
    list_cat=[]
    list_session=[]
    for cat in category:
       
           list_cat.append({"name":cat.Category_name,"id":cat.id,"has_session":cat.has_session,"is_sub":cat.is_sub}) 
    for s in session:
        list_session.append({'name':s.name,'year':s.year,'id':s.id})
        
    data={
        "session":list_session,
        "category":list_cat
    }
    return JsonResponse(data,safe=False)    
        

################## SESSION VIEW #####################
def SessionTable(request):
    query=SessionModel.objects.filter(publish=True)
    new_list=list(query.values())
    n_list=[{'id':k['id'],'name':k['name'],'year':k['year'],'publish':"Active" if k['publish']==True else 'Inactive'} for k in new_list]
    print('n_list: ',n_list)

    return JsonResponse(n_list,safe=False)  
def Session(request):
    if request.method == "POST":
        frm=SessionForm(request.POST)
        
        if frm.is_valid():
            frm.save()
            messages.success(request,'Session created')
            return redirect('session')
      
    frm=SessionForm()
    context={
    'form':frm        
    }
    return render(request,'nestedapp/session.html',context)
def SessionSave(request):
    JsonResponse({'success':True})
    
def SessionUpdate(request,id):
    if request.method=="POST":
        instance=SessionModel.objects.get(pk=id)
        form=SessionForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Session has been Updated successfully")
            return redirect('session')
    
    instance = SessionModel.objects.get(pk=id)
    

    form = SessionForm(instance=instance)
    print(instance.year)
   
    
    context={
        "form":form,
        "instance":json.dumps(model_to_dict(instance))
    }
    return render(request,'nestedapp/sessionUpdate.html',context)

################### SEMESTER VIEW ####################

def semesterPage(request):
    return render(request,'nestedapp/semList.html')

def SemesterCourse(request,id):
    sem_ins=Semester.objects.get(pk=id)
    print(sem_ins)
    context={
        "data":sem_ins.level
    }
    return render(request,'nestedapp/sem_course.html',context)


def AddCourseToSemester(request):
    category=Category.objects.all()
    department=Depertment.objects.all()
    course=CourseModel.objects.all()
    
    category_list=[]
    department_list=[]
    course_list=[]
    for cat in category:
        category_list.append({'name':cat.Category_name,'id':cat.id,'has_session':cat.has_session,'is_sub':cat.is_sub})
    for dep in department:
        department_list.append({'id':dep.id,'name':dep.depName,'category':dep.category.id,})
    for c in course:
        course_list.append({'id':c.id,'name':c.name,"category":c.category.id,'department':c.department.id})
        
    data={
        'category':category_list,
        'department':department_list,
        'course':course_list
    }    
    return JsonResponse(data,safe=False)

def PostCourse(request):
    if request.method == "POST":
        data=json.loads(request.body)
        sem_ins=Semester.objects.filter(level=data["semester"])
        for sem in sem_ins:
            sem.course.add(data['course'])
            
    return JsonResponse({"success":True})

    


################### CONTROLLING VIEW ################
def ControlingView(request):
    # frm=EndwiseCourseForm()
    # context={
    #     'form':frm
    # }
    return render(request,'nestedapp/courseControl.html')    

def ControlPost(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        semesters=data['semesters']
        print(semesters)
        sessionCategory=SessionCategory(session_id=data['session'],category_id=data['category'],total_semester=data['total_semesters'])
        sessionCategory.save()
        session_cat=SessionCategory.objects.filter(session__id=data['session'],category__id=data['category'])
        print(session_cat)
        
       
        for d in semesters:
            semester=Semester(level=d['level'],startDate=d['semester_start'],endDate=d['semester_end'])
           
            
            
            
            semester.save()
            
           
            for s_c in session_cat:
                
                s_c.semester.add(semester)
                
                  
        
        
            
    return JsonResponse({'sussess':True})

################### SERIALIZE VIEW ################

class categoryView(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CatSerializer
    
class DepartmentView(ListAPIView):
    queryset=Depertment.objects.all()
    serializer_class=DepertSerializer
class SemesterView(ListAPIView):
    queryset=Semester.objects.all()
    serializer_class=SemesterSerializer
class SubjectView(ListAPIView):
    queryset=Subject.objects.all()
    serializer_class=SubSerializer            
class TopicView(ListAPIView):
    queryset=videoTopic.objects.all()
    serializer_class=TopicSerializer      
    
    
class PackView(ListAPIView):
    queryset=Package.objects.all()
    serializer_class=PackageSerialize
    
class Videosview(ListAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerialize        
    
class ChapSview(ListAPIView):
    queryset=Chapter.objects.all()
    serializer_class=ChapSerializer    
    
class CourseSview(ListAPIView):
    queryset=  CourseModel.objects.all()
    serializer_class=CourseSerialize  
class InstructorSview(ListAPIView):
    queryset=Instructor.objects.all()
    serializer_class=InstSerialize    

class SessionCatSerialView(ListAPIView):
    queryset=SessionCategory.objects.all()
    serializer_class=SessionCatSerial   

class SessionSerialView(ListAPIView):
    queryset=SessionModel.objects.all()
    serializer_class= SessionSerial   