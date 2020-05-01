from rest_framework import serializers
from .models import Technique


class TechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technique
        fields = ('name', 'instructions', 'image_url',
                  'user', 'video_url')
