from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
urlpatterns=[

     path("", views.home, name="home"),
     path("createAnnouncement/", views.createAnnouncement, name="create-announcement"),
     path("createCommission/", views.createCommission, name="create-commission"),
     path("createLesson/", views.createLesson, name="create-lesson"),
     path("createNews/", views.createNews, name="create-news"),
     path("createSponsor/", views.createSponsor, name="create-sponsor"),
     path("login/", views.loginPage, name="login-page"),
     path("logout/", views.logoutUser, name="logout"),
     path("delete_announce/<str:pk>", views.deleteAnnouncement, name="delete-announce"),
     path("delete_lesson/<str:pk>", views.deleteLesson, name="delete-lesson"),
     path("delete_commission/<str:pk>", views.deleteCommission, name="delete-commission"),
     path("delete_news/<str:pk>", views.deleteNews, name="delete-news"),
     path("delete_sponsor/<str:pk>", views.deleteSponsor, name="delete-sponsor"),
     path("updateAnnouncement/<str:pk>",views.updateAnnouncement,name="update-announce"),
     path("updateLesson/<str:pk>",views.updateLesson,name="update-lesson"),
     path("updateCommission/<str:pk>",views.updateCommission,name="update-commission"),
     path("updateNews/<str:pk>",views.updateNews,name="update-news"),
     path("updateSponsor/<str:pk>",views.updateSponsor,name="update-sponsor"),
    
     
]
     


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)