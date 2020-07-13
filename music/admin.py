from django.contrib import admin
from .models import Album, Song
from music.models import Song,Album

class SongAdmin(admin.ModelAdmin):
    list_display = ('song_title','album','audio_file','is_favorite','is_private')
    search_fields = ('song_title','album')
    # ordering = ('-song_title',)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_title','artist','user','genre','album_logo','is_favorite')
    search_fields = ('album_title','artist')


admin.site.register(Album,AlbumAdmin)
admin.site.register(Song,SongAdmin)
