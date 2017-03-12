from django.contrib import admin
# Register your models here.
from django.core.exceptions import PermissionDenied
from django.db.models.aggregates import Count

from voting.admin_form import VoteAdminForm
from voting.models import Votes, VotingParams, Booth


class VoteAdmin(admin.ModelAdmin):

    list_display = ('voter', 'get_candidate', 'get_parameter', 'get_booth', 'created_at', 'comments', 'get_winner')
    list_filter = ('voter', 'candidate__name', 'booth__booth_name', 'created_at')
    list_per_page = 10
    search_fields = ['voter']

    def save_model(self, request, obj, form, change):
        if request.user != form.cleaned_data.get("voter"):
            raise PermissionDenied()
        if form.cleaned_data.get("voter").name == form.cleaned_data.get("candidate").name:
            raise Exception("Cannot vote to yourself")
        if Votes.objects.filter(voter=form.cleaned_data.get("voter"), parameter=form.cleaned_data.get("parameter")).\
                exists():
            raise Exception("Already Voted For %s Parameter" % (form.cleaned_data.get("parameter"), ))

    def get_queryset(self, request):
        return super(VoteAdmin, self).get_queryset(request).filter(booth__is_active=True)

    def get_candidate(self, obj):
        return obj.candidate.name
    get_candidate.short_description = 'Candidate'
    get_candidate.admin_order_field = 'candidate__name'

    def get_booth(self, obj):
        return obj.booth.booth_name
    get_booth.short_description = 'Booth'
    get_booth.admin_order_field = 'booth__booth_name'

    def get_parameter(self, obj):
        return obj.parameter.parameter_name
    get_parameter.short_description = 'Parameter'
    get_parameter.admin_order_field = 'parameter__parameter_name'

    def get_winner(self, obj):
        dict_list = Votes.objects.filter(booth=obj.booth).values("candidate__name"). \
            annotate(vote_count=Count("id"))
        seq = max(dict_list, key=lambda x: x['vote_count'])
        return seq.get("candidate__name")
    get_winner.short_description = 'Winner'


admin.site.register(Votes, VoteAdmin)


class BoothAdmin(admin.ModelAdmin):

    list_display = ('booth_name',)
    search_fields = ['booth_name']

admin.site.register(Booth, BoothAdmin)

class ParamAdmin(admin.ModelAdmin):

    list_display = ('parameter_name',)
    search_fields = ['parameter_name']

admin.site.register(VotingParams, ParamAdmin)