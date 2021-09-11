"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #here we liked the default path to index and about path to show about context
    # it has 3 arguments 
        # first one is for path like after the domain name / first argument
        # second argument is for the function where we have written the content like what we wanted to show
        # third we have assinged this path as a name we will see this later why the name is being used
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('firstCaps', views.firstCaps, name = 'firstCaps'),
    path('spaceRemove', views.spaceRemove, name = 'spaceRemove'),
    path('charCount', views.charCount, name = 'charCount')
]
