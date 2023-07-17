from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import VideoServiceUser

from allauth.socialaccount.forms import SignupForm


class VideoServiceUserCreationForm(UserCreationForm):

    class Meta:
        model = VideoServiceUser
        fields = ('username', 'email', 'phone_number')


class VideoServiceUserChangeForm(UserChangeForm):

    class Meta:
        model = VideoServiceUser
        fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')


class VideoServiceSocialSignupForm(SignupForm):
    phone_number = forms.CharField(max_length=11, label='phone_number')

    def __init__(self, *args, **kwargs):
        super(VideoServiceSocialSignupForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'] = forms.CharField(required=True)

    def save(self, request):
        user = super(VideoServiceSocialSignupForm, self).save(request)
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()

        return user

    def signup(self, request, user):
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
