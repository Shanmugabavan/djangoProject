from django.contrib import admin

# Register your models here.
from .models import University

class Universityadmin(admin.ModelAdmin):
    list_display=('id','uni_name','uni_address','phone_number',) #for admin panel like datebase
    list_display_links = ('id','uni_name')
    list_filter = ('uni_name',) #for filtering
    list_editable = ('phone_number',)
    search_fields = ('uni_name',)
    list_per_page = 25
admin.site.register(University,Universityadmin)

