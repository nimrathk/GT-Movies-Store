from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

class CustomUserCreationForm(UserCreationForm):
    security_answer = forms.CharField(
        max_length=100,
        required=True,
        label="Security Question: What city were you born in?",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1',
        'password2', 'security_answer']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )
        self.order_fields(['username', 'password1', 'password2', 'security_answer'])

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                security_question="What city were you born in?",
                security_answer=self.cleaned_data['security_answer']
            )
        return user