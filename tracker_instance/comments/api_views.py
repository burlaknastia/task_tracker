from django_comments.models import Comment
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from tracker_instance.comments.serializers import CommentsSerializer


class CommentsList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        site = get_current_site(request)
        user = request.user
        payload['site'] = payload['site'] if payload.get('site') is not None else site.pk
        payload['user'] = payload['user'] if payload.get('user') is not None else user.id
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)