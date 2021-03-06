from rest_framework import serializers
from .models import Action


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    action_id = serializers.ReadOnlyField()
    data = serializers.JSONField()

    class Meta:
        model = Action
        read_only_fields = ('time', 'randomness', 'version')

    def create(self, validated_data):
        action = Action(**validated_data)
        return action
