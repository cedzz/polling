from django.contrib import admin
# Register your models here.
from sprints.models import Projects, Sprints


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('project_name',)
    search_fields = ['project_name']

admin.site.register(Projects, ProjectAdmin)

class SprintAdmin(admin.ModelAdmin):

    list_display = ('sprint_name',)
    search_fields = ['sprint_name']

admin.site.register(Sprints, SprintAdmin)