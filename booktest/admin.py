# -*- coding:UTF-8 -*-

from django.contrib import admin

# Register your models here.
from models import *

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

# class HeroInfoInline(admin.TabularInline):
#     model = HeroInfo
#     extra = 3


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_data']
    list_filter = ['btitle','bpub_data']
    search_fields = ['btitle']
    list_per_page = 5
    fieldsets = [
        (u'基本信息',{'fields':['btitle']}),
        (u'扩展信息',{'fields':['bpub_data']})
    ]
    inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname','gender']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
