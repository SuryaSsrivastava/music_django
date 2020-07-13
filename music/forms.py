from django import forms
from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']
        widgets = {
        'artist' : forms.TextInput(attrs={'placeholder': 'Artist name'}),
        'album_title' : forms.TextInput(attrs={'placeholder': 'Album_title'}),
        'genre' : forms.TextInput(attrs={'placeholder': 'Genre'}),
        # 'album_logo' : forms.PasswordInput(attrs={'placeholder': 'Choose Your file'}),
}

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']
        widgets = {
        'song_title' : forms.TextInput(attrs={'placeholder': 'Song_title'}),
        # 'audio_file' : forms.TextInput(attrs={'placeholder': 'Audio_file'}),
        
}



