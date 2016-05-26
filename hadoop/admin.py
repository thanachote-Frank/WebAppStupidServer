from django.contrib import admin
from hadoop.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'input', 'result')

admin.site.register(Job, JobAdmin)
