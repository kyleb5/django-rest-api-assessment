"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist
"""Create a Song
Delete a Song
Update a Song
View a List of all the Songs
Details view of a single Song and its associated genres and artist details"""


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
