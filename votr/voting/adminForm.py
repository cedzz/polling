from django import forms

from voting.models import Votes


class VoteAdminForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = '__all__'
    voter = forms.CharField(disabled=True)

    def clean(self):

        if self.cleaned_data.get("voter").name == self.cleaned_data.get("candidate").name:
            raise forms.ValidationError("Self voting is not allowed")
        if Votes.objects.filter(voter=self.cleaned_data.get("voter"), parameter=self.cleaned_data.get("parameter"),
                                booth=self.cleaned_data.get("booth")). \
                exists():
            raise forms.ValidationError("Already Voted For %s Parameter" % (self.cleaned_data.get("parameter")))