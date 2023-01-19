from django import forms
from .models import User
from . models import UserProfile
from . Validator import allow_only_image
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    conform_password = forms.CharField(widget=forms.PasswordInput(),min_length=8)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        conform_password = cleaned_data.get('conform_password')
        if password != conform_password:
            raise forms.ValidationError("Passwords didn't match.")

class UserProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'start typing...', 'required': 'required'}))
    profile_picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_image])
    cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_image])
    latitude = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    longitude = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_photo', 'address', 'country', 'state', 'city', 'pin_code', 'latitude', 'longitude']

    # def __init__(self, *args, **kwargs):
    #     super(UserProfileForm,self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         if field == 'latitude' or 'longitude':
    #             self.fields[field].widget.attrs['readonly'] = 'readonly'

class UserInfoForm(forms.ModelForm):
    class Meta:
        model =User
        fields = ['first_name','last_name','phone_number']
