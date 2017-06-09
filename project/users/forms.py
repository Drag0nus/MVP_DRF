from django import forms

from .models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['id']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
