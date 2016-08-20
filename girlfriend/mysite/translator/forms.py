from django import forms
from .models import user_input

class userinput_form(forms.ModelForm):

	class Meta:
		model = user_input
		fields = content