from django.urls import path
from .import views
from django.contrib.auth.models import User, auth

urlpatterns=[
	path('',views.home,name="home"),
	path('about',views.about,name="about"),
	path('contact',views.contact,name="contact"),
	path('studentfeedback',views.studentfeedback,name="studentfeedback"),
	path('sucess',views.sucess,name="sucess"),
	path('teacherdetails',views.teacherdetails,name="teacherdetails"),
	path('teacherhome',views.teacherhome,name="teacherhome"),
    path('viewfeedback',views.viewfeedback,name="viewfeedback"),

    path("signup/",views.register,name="reg"),
    path("user_login/",views.user_login,name="user_login"),
    path('accounts/login/login',views.user_login, name="login"),
    path('accounts/login/user_login',views.user_login, name="login"),
    path('accounts/login/user_login',views.user_login,name="user_login"),
    path("signup/login",views.user_login,name="user_login"),

]