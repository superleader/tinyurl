from django.contrib.auth.models import User
from django.db.models import Model, URLField, ForeignKey, CharField


class URL(Model):
    original = URLField('original URL', unique=True)
    user = ForeignKey(User)
    slug = CharField(max_length=255)