from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from tracker_instance.descriptions.serializers import DescriptionSerializer
from tracker_instance.models import Description


class DescriptionsList(ListCreateAPIView):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


class DescriptionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    lookup_field = 'id'
