from django.urls import path
from . import views

urlpatterns = [

    # # path('home/', views.home, name="home"),
    # path('display/',views.display,name="display"),
    path('details/<id>', views.details, name="details"),
    path('studentdetails/', views.studentdetails, name="studentdetails"),
    path('create/', views.create, name="create"),
    path('createstudent/', views.createstudent, name="createstudent"),
    path('signup/', views.signup, name="signupForm"),
    path('userdetail/',views.user_details,name="userdetail"),
    path('userview/', views.viewUser, name="userview"),
    path('getstudent/', views.getstudentdetails, name="getstudentdetails"),
    path('getname/', views.getname, name="getname"),
    path('getdetails/<id>/', views.getdetails, name="getdetails"),
    path('deletedetails/<id>/', views.deletedetails, name="deletedetails"),
    path('emailsend/', views.emailSend, name="emailsend"),
    path('emailnew/', views.newmail, name="emailnew"),
    path('api/', views.ListStudent.as_view()),
    path('<int:pk>/', views.DetailStudent.as_view()),
    path('search/',views.search, name="search"),
    path('login/',views.loginuser, name="login"),
    path('viewsession/',views.sessofuser, name="viewsession"),
    path('page/',views.home,name="page")
]