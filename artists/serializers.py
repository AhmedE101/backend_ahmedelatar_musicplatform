from rest_framework import serializers
from artists.models import Artist


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ['id', 'stage_name', 'social_link']

    def create(self, validated_data):
        """
        Create and return a new `Artist` instance, given the validated data.
        """
        return Artist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Artist` instance, given the validated data.
        """
        instance.stage_name = validated_data.get(
            'stage_name', instance.stage_name)
        instance.social_link = validated_data.get(
            'social_link', instance.social_link)
        instance.save()
        return instance
