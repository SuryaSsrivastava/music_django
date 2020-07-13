from django.contrib.auth.models import Permission
from django.db import models
from accounts.models import Account

class Album(models.Model):
    user = models.ForeignKey(Account, default=1,on_delete=models.SET_DEFAULT)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.song_title
