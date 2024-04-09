from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Event
from django.http import Http404


class EventView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def event(self, request):
        title=request.data.get('title')
        content=request.data.get('content')
        description=request.data.get('description')

        if not title or content:
            return Response({"Error": "Missing Required Fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.role!='CL':
            return Response({"Error": "Only Clubs can post Events"}, status=status.HTTP_400_BAD_REQUEST)
        
 
        
        event=Event.objects.create(title=title, content=content,description=description,club=request.user, created_at=timezone.now(), updated_at=timezone.now())

        return Response({"message":"Event posted successfully", "event": {
            "id"=event.id,
            "title":event.title,
            "content":str(event.content),
            "description":event.description,
            "club": event.club.username,
            "created_at": event.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": event.updated_at.strftime('%Y-%n-%d %H:%M:%S')
        }},status=status.HTTP_201_CREATED)
    
class EventDetailView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get_object(self,pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        event=self.get_object(pk)
        return Response({
            "id":event.id,
            "title":event.title,
            "content":str(event.content),
            "description":str(event.description),
            "created_at": event.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": event.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    def put(self, request, pk, format=None):
        event=self.get_object(pk)
        title=request.data.get('title',event.title)
        content=request.data.get('content',event.content)
        description=request.data.get('description', event.description)


        event.title=title
        event.content=content
        event.description=description
        event.save()

        return Response({
            "message":"Post updated successfully",
            "event":{
                "id":event.id,
                "title":event.title,
                "content":str(event.content),
                "description":str(event.description),
                "created_at": event.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": event.updated_at.strftime('%Y-%m-%d %H:%M:%S')

            }
        }, status=status.HTTP_200_OK)
    
    def delete(self, request, pk, format=None):
        event=self.get_object(pk)
        event.delete()
        return Response({"message":"post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
        

