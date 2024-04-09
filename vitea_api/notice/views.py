from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Notice
from .serializers import NoticeSerializer
from rest_framework.views import APIView
#views
#creating a post
class NoticeCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get,update and delete
class NoticeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
