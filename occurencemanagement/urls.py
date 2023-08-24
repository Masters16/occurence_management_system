"""bloodbankmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from appointments import views as a_views
from blood import views
from police import views as p_views
from user import views as u_views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name=''),
    path('logout', LogoutView.as_view(template_name='blood/logout.html'), name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),

#Police urls
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('login', LoginView.as_view(template_name='police/adminlogin.html'), name='login'),
    path('police-dashboard', p_views.police_dashboard_view, name='police-dashboard'),
    path('police/create-record', p_views.add_occurence_view, name='create-record'),
    path('police/update-record', p_views.occurence_records_view, name='update-record'),
    path('police/register-user', p_views.add_user_record, name='create-record'),
    path('police/occurence-reports/', p_views.occurence_report_view, name="occurence-reports"),
    path('police/users-reports/', p_views.user_report_view, name="users-reports"),
    path('police/generate-occurence-report/', p_views.generate_occurence_report, name="generate-occurence-report"),
    path('police/generate-user-report/', p_views.generate_users_report, name="generate-user-report"),
    path('download-user-report/<str:pk>', p_views.download_user_report, name="download-user-report"),
    path('download-occurence-report/<str:pk>', p_views.download_occurence_report, name="download-occurence-report"),

    #User urls
    path('user-dashboard', u_views.user_dashboard_view, name='user-dashboard'),
    path('user/view-records', u_views.occurence_records_view, name='view-records'),



]
