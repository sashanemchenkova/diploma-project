from django import forms
from .models import Gender, Goal, Activity, Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

User = get_user_model()


class UserDailyNorm(forms.Form):
    current_weight = forms.FloatField(min_value=0.0, label=' Your current weight(kg)')
    current_height = forms.FloatField(min_value=0.0, label='Your height(cm)')
    age = forms.IntegerField(min_value=0, label='Your age')
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), label='Enter your gender', widget=forms.RadioSelect)
    activity_level = forms.ModelChoiceField(queryset=Activity.objects.all(), label='Choose your level activity',
                                            widget=forms.RadioSelect)
    goal = forms.ModelChoiceField(queryset=Goal.objects.all(), label='Choose your goal', widget=forms.RadioSelect)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", 'last_name', "email")


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", 'last_name', "email", "password1", "password2",)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user
