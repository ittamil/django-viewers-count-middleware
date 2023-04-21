from django.contrib import admin
from request_viewer_counts_middleware.models import *


@admin.register(ViewersCount)
class ViewersCountModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'path','views','ipaddress','date_created')
    list_display_links = ['id', 'path','views','ipaddress','date_created']
    search_fields = ['id', 'path','views','ipaddress','date_created']

