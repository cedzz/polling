from django.contrib import admin
# Register your models here.
from django.contrib import messages

from sprints.models import Projects, Sprints, SprintSummary


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('project_name',)
    search_fields = ['project_name']

admin.site.register(Projects, ProjectAdmin)


class SprintAdmin(admin.ModelAdmin):

    list_display = ('sprint_name', 'created_at', 'is_active', 'start_date', 'end_date')
    search_fields = ['sprint_name']


admin.site.register(Sprints, SprintAdmin)


class SprintSummaryAdmin(admin.ModelAdmin):

    list_display = ('sprint_name', 'member', 'ticket', 'ticket_desc', 'points', 'due_date', 'status')
    search_fields = ['ticket', 'member', 'due_date', 'status']
    readonly_fields = ('sprint_name', 'member', 'ticket', 'ticket_desc', 'points', 'due_date', 'status')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        return super(SprintSummaryAdmin, self).get_queryset(request).filter().order_by('-points')

admin.site.register(SprintSummary, SprintSummaryAdmin)