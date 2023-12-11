"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist


class ArtistView(ViewSet):
    """Django Rest Api Assessment"""

    def retrieve(self, request, pk):
        """Handle GET requests for artist type
        Returns:
            Response -- JSON serialized event
        """
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def list(self, request):
        """Hnadle GET requests to get all artists

        Returns:
            Response -- JSON serialized list of artist
            """
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle CREATE requests to create an artist"""
        artist = Artist.objects.create(
            name=request.data["name"],
            age=request.data["age"],
            bio=request.data["bio"],
        )
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle UPDATE requests for artists
        """

        artist = Artist.objects.get(pk=pk)
        artist.name = request.data["name"]
        artist.age = request.data["age"]
        artist.bio = request.data["bio"]
        artist.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        artsit = Artist.objects.get(pk=pk)
        artsit.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ArtistSerializer(serializers.ModelSerializer):
    """JSON serializer for artist
    """

    class Meta:
        model = Artist
        fields = ('id', 'name', 'age', 'bio')
