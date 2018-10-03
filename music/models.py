from django.db import models
from django.urls import reverse


# Create your models here.

class Album(models.Model):
	artist = models.CharField(max_length=250, help_text='Artist Name who Song the Songs')
	album_title = models.CharField(max_length=500, help_text='Album Name')
	genere = models.CharField(max_length=100, help_text='Genere: Classic, Rock etc.')
	album_logo = models.CharField(max_length=1000, help_text='Logo of Album must be an "url"')

	def __str__(self):
		return self.artist+'-'+self.album_title

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.pk})

class Song(models.Model):
	SONG_TYPE = (
		('-1', 'Select Type'),
		('mp3', 'Audio'),
		('mp4', 'Mobile Video'),
		('3gp', 'LQ Video'),
		('hd', 'HD Video')
	)
	album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='album name')
	file_type = models.CharField(max_length=10, choices=SONG_TYPE, default='-1')
	song_title = models.CharField(max_length=250)
	is_favourite = models.BooleanField(default=False)

	def __str__(self):
		return self.song_title+'.'+self.file_type

class Comments(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	comment = models.TextField(max_length=250)

	def __str__(self):
		return self.comment

	


		
