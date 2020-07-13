from rest_framework import serializers

from .models import Album,Song

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('user', 'artist','album_title','genre','album_logo','is_favorite')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Song
        fields = ('album','song_title','audio_file','is_favorite','is_private')