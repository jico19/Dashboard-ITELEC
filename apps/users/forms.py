from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {  # <- plural
            "username": forms.TextInput(attrs={
                "placeholder": "username"
            }),
            "password": forms.PasswordInput(attrs={
                "placeholder": "password"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css = "w-full px-3 py-2 border rounded"

            # base class
            field.widget.attrs["class"] = css

            # optional per-field logic
            if name in ["description", "notes"]:
                field.widget.attrs["class"] += " h-32"

            # add placeholder automatically
            field.widget.attrs.setdefault(
                "placeholder",
                name.replace("_", " ").title()
            )


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "username"
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "password"
        }
    ))