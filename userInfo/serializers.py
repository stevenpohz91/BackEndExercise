from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        #define the model I want django to serialize
        model = Profile
        #and the follow is the field that django need to serialize
        fields = ('name','email')
        #alternatively, if return all > fields = '__all__'