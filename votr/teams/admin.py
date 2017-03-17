from django.contrib import admin
from django.core.exceptions import PermissionDenied

from .models import Teams, Members


# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    list_display = ('team_name',)
    search_fields = ['team_name']
    list_filter = ('team_name', 'company', 'created_at')
    list_per_page = 10

admin.site.register(Teams, TeamAdmin)


class MemberAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name', 'team__team_name', 'created_at', 'is_active')
    search_fields = ['name']
    readonly_fields = ('user', )

    def get_queryset(self, request):
        return super(MemberAdmin, self).get_queryset(request).filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if request.user != obj.user:
            raise PermissionDenied()

admin.site.register(Members, MemberAdmin)
