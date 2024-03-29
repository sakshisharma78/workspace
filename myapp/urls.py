from django.urls import path
from . import views

urlpatterns = [

    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("invalid",views.invalid,name="invalid"),
    path("",views.home,name="home"),
    path("footer",views.footer,name="footer"),
    path("myteam",views.myteam,name="myteam"),
    path("offers",views.offers,name="offers"),
    path("header",views.header,name="header"),
     path("recorded_sessions",views.recorded_sessions,name="recorded_sessions"),

]