from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['customer_name'].label = ''
        self.fields['email'].label = ''
        self.fields['form_message'].label = ''

    class Meta:
        model = Feedback
        exclude = []
        widgets = {
            'customer_name': forms.TextInput(attrs={"placeholder": "Ваше имя"}),
            'email': forms.TextInput(attrs={"placeholder": "E-mail"}),
            'form_message': forms.TextInput(attrs={"placeholder": "Сообщение"}),
        }
