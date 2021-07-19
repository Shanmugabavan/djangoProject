from django.contrib import admin

# Register your models here.
from .models import Member

class Memberadmin(admin.ModelAdmin):
    list_display=('id','name','university','age','address') #for admin panel like datebase
    list_display_links = ('id','name')
    list_filter = ('name',) #for filtering
    list_editable = ('age',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Member,Memberadmin)