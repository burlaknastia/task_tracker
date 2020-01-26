from rest_framework.serializers import ModelSerializer

from tracker_instance.models import Description


class DescriptionSerializer(ModelSerializer):
    class Meta:
        model = Description
        fields = ('id', 'content')
