from rest_framework import serializers
from API.models import ShortUrl

class ShortUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ('url', 'short_code')

    def create(self, validated_data):
        url = ShortUrl.objects.create(**validated_data)
        return url