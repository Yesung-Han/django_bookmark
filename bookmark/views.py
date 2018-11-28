# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#import Pre-served gerneric View 
from django.views.generic import ListView, DetailView
#import Bookmark model to lookup Bookmark DB table
from bookmark.models import Bookmark

# Create your views here.

#---ListView 
# when url pattern 1 : r'^bookmark/$' come, connected this class
class BookmarkLV(ListView):
    #this class is view based on Bookmark DB table 
    model = Bookmark
    #jango automatically make 2 properties
    # 1. context variable : object_list
    # 2. templet html file : automatically named 'modelname_list.html'

class BookmarkDV(DetailView):
    model = Bookmark
    #jango automatically make 2 properties
    # 1. context variable : object_list
    # 2. templet html file : automatically named 'modelname_detail.html'