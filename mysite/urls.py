"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from bookmark.views import BookmarkLV, BookmarkDV
#from bookmark.views import *


urlpatterns = [
    #to get admin URLconf 
    #can also use include() func to get already defined URLconf
    #-> url(r'^admin/', include(admin.site.urls))
    #in admin case, usually don't use includ() func.
    url(r'^admin/', admin.site.urls),

    #Class-based view for bookmark app

    # url pattern 1 : r'^bookmark/$' come -> view class BookmarkDV is manage this url, 
    # url pattern 1 's name is 'index'  
    url(r'^bookmark/$',BookmarkLV.as_view(),name = 'index'),
    url(r'^bookmark/(?P<pk>\d+)/$',BookmarkDV.as_view(),name = 'detail'),
]
