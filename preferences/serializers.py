from rest_framework import serializers
from .models import Interaction, User
import logging

logger = logging.getLogger(__name__)

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['post', 'user', 'interaction_type', 'interaction_time']

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'tags' 'preferences']
