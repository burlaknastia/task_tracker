from django.urls import path

from tracker_instance.description.api_views import DescriptionsList, DescriptionDetail

urlpatterns = [
    path('', DescriptionsList.as_view(), name='api-descriptions-list'),
    path('<int:id>/', DescriptionDetail.as_view(), name='api-description-detail'),
]
