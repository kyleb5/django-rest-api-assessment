from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist


class SongView(ViewSet):
    """Django Rest Api Assessment"""

    def retrieve(self, request, pk):
        """Handle GET requests for artist type
        Returns:
            Response -- JSON serialized event
        """
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET rquests to get all songs

        Returns:
            Response -- JSON serialized list of songs"""
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle CREATE requests to create a song"""
        artist_id = Artist.objects.get(pk=request.data["artist_id"])
        song = Song.objects.create(
            title=request.data["title"],
            album=request.data["album"],
            length=request.data["length"],
            artist_id=artist_id,
        )
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle UPDATE rtequests for songs"""
        song = Song.objects.get(pk=pk)
        song.title = request.data["title"]
        song.album = request.data["album"]
        song.length = request.data["length"]
        artist = Artist.objects.get(pk=request.data["artist_id"])
        song.artist_id = artist
        song.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for song"""

    class Meta:
        model = Song
        fields = ('id', 'title', 'artist_id', 'album', 'length')
