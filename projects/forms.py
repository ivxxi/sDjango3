from .models import Project,UserProfile
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title','project_description','landing_page','live_site')


class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','bio', 'contact')
