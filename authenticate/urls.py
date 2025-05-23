"""
URL configuration for gtu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from authenticate import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.login_user,name="login"),
    path('home/',views.home,name='home'),
    path('user_record/',views.user_record,name='user_record'),
    path('register/',views.register,name="register"),
    path('login/',views.login_user, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('user_data/<int:pk>',views.user_data,name='user_data'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit-user'),
    path('change-password/<int:user_id>/', views.change_user_password, name='change_user_password'),
]


