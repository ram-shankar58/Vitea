from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notes
from django.http import HttpResponse

from django.shortcuts import get_object_or_404

class NoteListCreateAPIView(APIView):
    def get(self, request):
        notes = Notes.objects.all()
        data = [{'id': note.id, 'title': note.title, 'description': note.description, 'created_at': note.created_at, 'content': note.content.url, 'author': note.author.username} for note in notes]
        return Response(data)

    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        content = request.data.get('content')
        if not (title and description and content):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
        note = Notes.objects.create(title=title, description=description, content=content, author=request.user)
        return Response({"message": "Note created successfully", "id": note.id}, status=status.HTTP_201_CREATED)

class NoteDetailAPIView(APIView):
    def get(self, request, pk):
        note = get_object_or_404(Notes, pk=pk)
        data = {'id': note.id, 'title': note.title, 'description': note.description, 'created_at': note.created_at, 'content': note.content.url, 'author': note.author.username}
        return Response(data)

    def put(self, request, pk):
        note = get_object_or_404(Notes, pk=pk)
        title = request.data.get('title')
        description = request.data.get('description')
        content = request.data.get('content')
        if not (title and description and content):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
        note.title = title
        note.description = description
        note.content = content
        note.save()
        return Response({"message": "Note updated successfully", "id": note.id})

    def delete(self, request, pk):
        note = get_object_or_404(Notes, pk=pk)
        note.delete()
        return Response({"message": "Note deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class NoteDownloadAPIView(APIView):
    def get(self, request, pk):
        note = get_object_or_404(Notes, pk=pk)
        if not note.content:
            return HttpResponse("Note content not found", status=status.HTTP_404_NOT_FOUND)

        file_path = note.content.path  # Assuming `content` is a FileField
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{note.title}.pdf"'  # Adjust filename as needed
            return response