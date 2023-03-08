from select import select
from selectors import SelectSelector
from django import forms
from taggit.forms import *
from .models import Category, Chapter, Depertment, Semester, Subject, Video,Package,Instructor,CourseModel,SessionModel,endCourse


class ParentForm(forms.ModelForm):
    
  
    class Meta:
        model= Category
        fields=['parent','Category_name','display_name','category_image','order','publish','has_session','is_sub']

        widgets={
            'parent':forms.Select(attrs={"class":"form-control"}),
            'Category_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter category name'}),
            'display_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a display name'}),
            'category_image':forms.ClearableFileInput(attrs={'class':'form-control',}),
           
            'order': forms.NumberInput(
                attrs={
                    'min':'0','class':'form-control','placeholder':'Enter number for ordering',
                }
            ),
            'publish':forms.CheckboxInput(attrs={'class':'form-control'}),
            'has_session':forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_sub':forms.CheckboxInput(attrs={'class':'form-control'})



        }


class DepForm(forms.ModelForm):
    class Meta:
        model=Depertment
        fields=['category','depName','shortName','dep_icon','dep_thumbnail','publish']

        widgets={
            "category":forms.Select(attrs={'class':'form-control'}),
            "depName":forms.TextInput(attrs={'class':'form-control'}),
            "shortName":forms.TextInput(attrs={'class':'form-control'}),
            "dep_icon":forms.ClearableFileInput(attrs={'class':'form-control',}),
            "dep_thumbnail":forms.ClearableFileInput(attrs={'class':'form-control',}),
           
            "publish":forms.CheckboxInput(attrs={'class':'form-control'}),
        }

# class SemForm(forms.ModelForm):
#     class Meta:
#         model= Semester
#         fields= ['name','category','department','startDate','endDate','icon','publish']  

#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control '}),
#             'category':forms.Select(attrs={"class":"form-control"}),
#             'department':forms.Select(attrs={"class":"form-control"}),
#             'startDate':forms.DateInput(attrs={"class":"form-control ","id":"startDate","type":"date",}),
#             'endDate':forms.DateInput(attrs={"class":"form-control ","id":"endDate","type":"date"}),
#             'icon':forms.ClearableFileInput(attrs={'class':'form-control'}),
#             "publish":forms.CheckboxInput(attrs={'class':'form-control'}),

#         }
class SubForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['name','category','subCode','publish','subImage','primaryColor','secondaryColor','order'] 
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'subCode':forms.NumberInput(attrs={'class':'form-control'}),
            'publish':forms.CheckboxInput(attrs={'class':'form-control'}),
            'subImage':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'primaryColor':forms.TextInput(attrs={'class':'form-control my-colorpicker1 colorpicker-element'}),
            'secondaryColor':forms.TextInput(attrs={'class':'form-control my-colorpicker1  colorpicker-element'}),
            'order':forms.NumberInput(attrs={'class':'form-control'})


        }   

# CHAPTER FORM
class ChapterForm(forms.ModelForm):
    class Meta:
        model=Chapter
        fields=['name','category','subject','publish']       

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'subject':forms.Select(attrs={'class':'form-control'}),
            'publish':forms.CheckboxInput(attrs={'class':'form-control'})
        }     


# VIDEO FORM
class VidForm(forms.ModelForm):
    class Meta:
        model= Video 
        fields=['name','tags','url','order','duration','description','publish','view','stream','thumbnail','video']   

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'tags':TagWidget(attrs={'data-role':'tagsinput','class':'form-control'}),
            'url':forms.TextInput(attrs={'class':'form-control'}),
            'order':forms.NumberInput(attrs={'class':'form-control'}),
            'duration':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'publish':forms.CheckboxInput(attrs={'class':'flat-red'}),
            'view':forms.CheckboxInput(attrs={'class':'flat-red'}),
            'stream':forms.CheckboxInput(attrs={'class':'flat-red'}),
            'thumbnail':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class':'form-control'})

        } 

   # PACKAGE FORM
class PackForm(forms.ModelForm):
    class Meta:
        model=Package     
        fields=['category','subject','chapter']
        widgets={
            'category': forms.Select(attrs={'class':'form-control','id':'select_cat','name':'sel-cat'}),
            'subject': forms.Select(attrs={'class':'form-control','id':'select_sub','placeholder':'Select subject','name':'sel-sub'}),
            'chapter':forms.Select(attrs={'class':'form-control','id':'select_chap','name':'sel-chap'})
        }   

    def __init__(self,*args, **kwargs) :
        super().__init__(*args,**kwargs)
        self.fields['subject'].queryset=Subject.objects.none()
        self.fields['chapter'].queryset=Chapter.objects.none()    

        if 'category' in  self.data:
            try:
                category_id=int(self.data.get('category'))
                self.fields['subject'].queryset=Subject.objects.get(category_id=category_id).order_by('name')
            except(ValueError,TypeError):
                pass    
        elif self.instance.pk:
            self.fields['subject'].queryset=self.instance.category.subject_set.order_by('name')    

        if 'subject' in self.data:
            try:
                subject_id=int(self.data.get('category'))
                self.fields['chapter'].queryset= Chapter.objects.get(subject_id=subject_id).order_by('name')
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['chapter'].queryset= self.instance.subject.chapter_set.order_by('name')     
            


class CourseForm(forms.ModelForm):
    
    class Meta:
       
        model=CourseModel
        fields=['name','category','department','subject','instructor','mentor','order','email','prerequisites','description','facebook','masenger','courseIcon','courseBanner','publish']      
        
        
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control','name':"course_name",'id':'couse_id'}),
            'category':forms.Select(attrs={'class':'form-control','name':'course_cat','id':'cat_id'}),
            'department':forms.Select(attrs={'class':'form-control ','name':'course_dep','id':'dep_id'}),
             'subject':forms.SelectMultiple(attrs={'class':'form-control','name':'subject','id':'sub_id'}),
            'instructor':forms.Select(attrs={'class':'form-control','name':'inst_name','id':'inst_id'}),
            'mentor':forms.Select(attrs={'class':'form-control','name':'mentor_name','id':'mentor_id'}),
            'order':forms.NumberInput(attrs={'class':'form-control','name':'order','id':'order_id'}),
            'email':forms.EmailInput(attrs={'class':'form-control','name':'email','id':'email_id'}),
            'prerequisites':forms.Select(attrs={'class':'form-control','name':'prerequisites','id':'pre_id'}),
            'description':forms.Textarea(attrs={'class':'form-control','name':'description','id':'des_id'}),
            'facebook':forms.TextInput(attrs={'class':'form-control','name':'facebook','id':'face_id'}),
            'masenger':forms.TextInput(attrs={'class':'form-control','name':'masenger','id':'masenger_id'}),
            'courseIcon':forms.ClearableFileInput(attrs={'class':'form-control ','name':'courseIcon','id':'icon_id'}),
            'courseBanner':forms.ClearableFileInput(attrs={'class':'form-control','name':'banner','id':'banner_id'}),
            'publish':forms.CheckboxInput(attrs={'class':'form-control'})
            
            
            
            
            
            
        }      
    def __init__(self,*args, **kwargs) :
        super(CourseForm,self).__init__(*args, **kwargs) 
    
        self.fields['department'].queryset=Depertment.objects.none()
        
        if 'category' in self.data:
            try:
                category_id=int(self.data.get('category'))
                self.fields['department'].queryset=Depertment.objects.filter(category_id=category_id).order_by('depName')
            except (ValueError,TypeError):
                pass     
            
        elif self.instance.pk:   
            self.fields['department'].queryset=self.instance.category.department_set.order_by('depName')


class instForm(forms.ModelForm):
    class Meta:
        model=Instructor
        fields=['name','department','organization','picture','available']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','name':'inst_name','id':'inst_id'}),
            'department':forms.Select(attrs={'class':'form-control','name':'inst_dep','id':'instDep'}),
            'organization':forms.TextInput(attrs={'class':'form-control','name':'org','id':'org_id'}),
            'picture':forms.ClearableFileInput(attrs={'class':'form-control','name':'inst_pic','id':'instPic'}),
            'available':forms.CheckboxInput(attrs={'class':'form-control','name':'inst_able','id':'instAble'})
        }            
        
class SessionForm(forms.ModelForm):
    class Meta:
        model=SessionModel
        fields=['name','year','publish'] 
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','required':"true"}),
            'year':forms.Select(attrs={'id':'id_year','placeholder':"Select a year...",'autocomplete':"off",'class':'form-control','required':'true'}),
            'publish':forms.CheckboxInput(attrs={'class':'form-control'})
          
        }      
        
 
class EndwiseCourseForm(forms.ModelForm):
    class Meta:
        model=endCourse
        fields=['name','category','days','is_active']  
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control',}),
            'category':forms.Select(attrs={'class':'form-control','id':'end_category','autocomplete':'off'}),
            'days':forms.NumberInput(attrs={'class':'form-control',}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-control'})
        }
                  
            