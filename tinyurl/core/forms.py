from uuid import uuid4
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.conf import settings

from core.models import URL


class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ('original',)
    
    def save(self):
      original = self.cleaned_data['original'].strip()
      instance = URL(original=original,
                user = User.objects.order_by('?').first(),
                slug = str(uuid4()).replace('-', '')[:settings.LEN])
      instance.save()
      return instance  
      
