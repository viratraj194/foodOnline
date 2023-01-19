from django import forms
from . models import Vendor,OpeningHours
from accounts.Validator import allow_only_image

class VendorForms(forms.ModelForm):
    vendor_license = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_image])

    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_license']


class OpeningHourForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = ['day','from_hour','to_hour','is_close']