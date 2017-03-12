from django.contrib import admin
from models import Teams, Members


# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    list_display = ('team_name',)
    search_fields = ['team_name']

admin.site.register(Teams, TeamAdmin)

class MemberAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Members, MemberAdmin)