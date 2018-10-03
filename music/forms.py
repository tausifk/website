from django.forms import ModelForm
from .models import Album
from .models import Comments

class AddAlbumForm(ModelForm):
	class Meta:
		model = Album
		fields = ['artist', 'album_title', 'genere', 'album_logo']

class UpdateAlbumForm(ModelForm):
	class Meta:
		model = Album
		fields = ['artist', 'album_title', 'genere', 'album_logo']

class CommentsForm(ModelForm):
	class Meta:
		model = Comments
		fields = ['comment']
