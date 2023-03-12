
from django.urls import path
from nestedapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('login/',views.loginview,name='login'),
   path('logout/',views.LogoutView,name='logout'),
   path('panel/',views.FrontView,name='panel'),
   path('',views.Dashboard,name='dash'),

  
 
   path("category/",views.CreateCategory,name='category'),
   path("category-list/",views.CategoryList,name='catlist'),
   path("category/<int:id>",views.CategoryUpdate,name='cat-update'),
   path("Delete/<int:id>",views.CategoryDelete,name='cat-delete'), 

  path('load-dep/',views.depload,name='load-dep'),
  path("department/",views.CreateDep,name='department'),
  path("dep-list/",views.DepList,name='dep-list'),
  path("dep-update/<int:id>",views.DepUpdate,name='dep-update'),
  path("dep-delete/<int:id>",views.depDelete,name='dep-delete'),

# URL FOR SEMESTER

 path('semester-list/',views.semesterPage,name='semester-list'),
 path("semester-course/<int:id>",views.SemesterCourse,name='semester-course'),



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
  
  # URL FOR COURSEVIEW
  path('course/',views.CourseView,name='course'),
  
  # URL FOR USER
  path('instructor/',views.InstView,name='instructor'),
  path('inst-api/',views.InstructorSview.as_view(),name='inst-api'),
  
  
  ################# table url ################
  
  # END DAY WISE
  path('end-day-wise/',views.endDayTable,name='end-day-wise'),
  path('end-add-course/<int:id>',views.endAddCourse,name='end-add-course'),
  path('load-course/',views.loadCourse,name='load-course'),
  path('laod-department/',views.loadDepartment,name='load-department'),
  
  
  
  
  
  #############  SERIALIZED URL   #############
  path('cat-api/',views.categoryView.as_view(),name='cat-api'),
  path('dep-api/',views.DepartmentView.as_view(),name='dep-api'),
  path('sem-api/',views.SemesterView.as_view(),name='sem-api'),
  path('sub-api/',views.SubjectView.as_view(),name='sub-api'),
  
  path('topic-video/',views.TopicView.as_view(),name='topic-video'),
  path('pack-api/',views.PackView.as_view(),name='pack-api'),
  path('video-api/',views.Videosview.as_view(),name='video-api'),
  path('chap-api/',views.ChapSview.as_view(),name='chap-api'),
  path('course-api/',views.CourseSview.as_view(),name='course-api'),
  
  
  path('response-table/',views.TableView,name="response-table"),
  path('table/',views.table,name='table'),
   path('new-response/',views.newDataTable,name='new-response'),
  path('newvid-list/',views.newVidList,name='newvid-list'),
  
  path('session/',views.Session,name='session'),
  path('session_save/',views.SessionSave,name='session_save'),
  path('session-table/',views.SessionTable,name='session-table'),
  path('session-update/<int:id>',views.SessionUpdate,name='session-update'),
  
  path('session-cat/api/',views.SessionCatSerialView.as_view(),name='session-cat/api'),
  path('session-api/',views.SessionSerialView.as_view(),name='session-api'),
  
  
  path('course-control/',views.ControlingView,name='course-control'),
  path('end-course-submit/',views.EndCouseSubmit,name='endSubmit'),
  path('control-post/',views.ControlPost,name='control-post'),
  
  
  path('session-and-category/',views.categoryAndSession,name='session-and-category'),
  
  
  path('addcourse-to-semester/',views.AddCourseToSemester,name='addcourse-to-semester'),
  path('post-course-semester',views.PostCourse,name='postCourse'),
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)