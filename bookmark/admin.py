# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#
from bookmark.models import Bookmark

# Register your models here.
#dddd
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Bookmark, BookmarkAdmin)