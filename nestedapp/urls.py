
from django.urls import path
from nestedapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('login/',views.loginview,name='login'),
   path('logout',views.LogoutView,name='logout'),
   path('panel/',views.FrontView,name='panel'),
   path('/',views.Dashboard,name='dash'),

  
 
   path("category/",views.CreateCategory,name='category'),
   path("category-list/",views.CategoryList,name='catlist'),
  path("category/<int:id>",views.CategoryUpdate,name='cat-update'),
  path("Delete/<int:id>",views.CategoryDelete,name='cat-delete'), 

  path("department/",views.CreateDep,name='department'),
  path("dep-list/",views.DepList,name='dep-list'),
  path("dep-update/<int:id>",views.DepUpdate,name='dep-update'),
  path("dep-delete/<int:id>",views.depDelete,name='dep-delete'),


  path("semester/",views.SemView,name='semester'),
  path("sem-list/",views.SemList,name='sem-list'),
  path("sem-update/<int:id>",views.semUpdate,name='sem-update'),
  path("sem-delete/<int:id>",views.semDelete,name='sem-delete'),


  #  URL FOR SUBJECT VIEW

  path("subject/",views.subPage,name='subject'),
  path("sub-list/",views.SubList,name='sub-list'),
  path("sub-update/<int:id>",views.SubUpdate,name='sub-update'),
  path("sub-delete/<int:id>",views.SubDelete,name='sub-delete'),

  # URL FOR CHAPTER
  path("chapter/",views.ChapList,name='chapter'),
  path("chap-update/<int:id>",views.ChapUpdate,name='chap-update'),
  path("chap-delete/<int:id>",views.ChapDelete,name='chap-delete'),

  # URL FOR VIDEO
  path('video/',views.VidView,name='video'),
  path('vid-list/',views.VideoList,name='vid-list'),
  path('vid-update/<int:id>',views.VidUpdate,name='vid-update'),
  path('vid-delete/<int:id>',views.VidDelete,name='vid-delete'),
  path('vid-details/<int:id>',views.VidDetails,name='vid-details'),

  # URL FOR PACKAGE
  path('package/',views.PackageView,name="package"),
  path('ajax-load/',views.loadSubject,name="ajax-load"),
  path('chapter-load/',views.loadChap,name="chapter-load"),
  path('video_search/',views.VidSearch,name='video_search'),
  
  # URL FOR VIDEO TOPIC
  path('topic/',views.topicView,name='topic'),
  
  
  
  
  
  #############  SERIALIZED URL   #############
  
  path('topic-video/',views.TopicView.as_view(),name='topic-video'),
  path('pack-api/',views.PackView.as_view(),name='pack-api'),
  path('video-api/',views.Videosview.as_view(),name='video-api')
  
  
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)