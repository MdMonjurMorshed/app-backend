from select import select
from selectors import SelectSelector

from tkinter.tix import Select
from turtle import width

from django import forms
from django.forms import CharField, Textarea, TextInput
from pyexpat import model
from taggit.forms import *

from .models import Category, Chapter, Depertment, Semester, Subject, Video,Package


class ParentForm(forms.ModelForm):
    
  
    class Meta:
        model= Category
        fields=['parent','Category_name','display_name','category_image','order','publish']

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
            'publish':forms.CheckboxInput(attrs={'class':'form-control'})



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

class SemForm(forms.ModelForm):
    class Meta:
        model= Semester
        fields= ['name','category','department','startDate','endDate','icon','publish']  

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control '}),
            'category':forms.Select(attrs={"class":"form-control"}),
            'department':forms.Select(attrs={"class":"form-control"}),
            'startDate':forms.DateInput(attrs={"class":"form-control ","id":"startDate","type":"date",}),
            'endDate':forms.DateInput(attrs={"class":"form-control ","id":"endDate","type":"date"}),
            'icon':forms.ClearableFileInput(attrs={'class':'form-control'}),
            "publish":forms.CheckboxInput(attrs={'class':'form-control'}),

        }
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