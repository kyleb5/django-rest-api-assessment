from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre


class GenreView(ViewSet):
    """Django Rest Api Assessment"""

    def retrieve(self, request, pk):
        """Handle GET requests for artist type
        Returns:
            Response -- JSON serialized event
        """
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def list(self, request):
        """Hnadle GET requests to get all genres
        """
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle CREATE equest to create an genre"""
        genre = Genre.objects.create(
            description=request.data["description"],
        )
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle UPDATE request for genre"""
        genre = Genre.objects.get(pk=pk)
        genre.description = request.data["description"]
        genre.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genre"""

    class Meta:
        model = Genre
        fields = ['id', 'description']
