from rest_framework import serializers

from DadJoke_api import models


class DadJokeSerializer(serializers.Serializer):
    """ Servializers a DadJoke fields"""
    joke_question = serializers.CharField(max_length=255)
    joke_answer   = serializers.CharField(max_length=255)
    groan_factor = serializers.IntegerField()


class DadJokeFeedItemSerializer(serializers.ModelSerializer):
    """Serializes DadJoke feed items """

    class Meta:
        model = models.DadJokeFeedItem
        fields = ('id', 'joke_question', 'joke_answer', 'groan_factor')
