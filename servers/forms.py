from django import forms
from .models import Servers


class ServerForm(forms.ModelForm):
    class Meta:
        model = Servers
        fields = ['server_name', 'server_ip', 'port']
