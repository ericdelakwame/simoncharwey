from rest_framework_gis.serializers import ModelSerializer
from accounts.models import (
    Profile, User
)

from studio.models import Category
from django.contrib.auth import get_user_model
from django_countries.serializers import CountryFieldMixin

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(CountryFieldMixin, ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields  = '__all__'