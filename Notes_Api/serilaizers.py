from rest_framework import serializers
from home.models import Notes


class Notes_Serilaizer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
