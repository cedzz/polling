from django import forms

from activity.models import ActivityBoard
from sprints.models import Sprints


class ActivityAdminForm(forms.ModelForm):
    class Meta:
        model = ActivityBoard
        fields = '__all__'

    def clean(self):

        if self.cleaned_data.get("sprint") != Sprints.objects.get(is_active=1):
            raise forms.ValidationError("Choose Active Sprint")