from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from . import views

app_name = 'music' #namespace required to identify correct url of a particular app while reversing/redirecting 

urlpatterns = [
#/music/
path ('', views.IndexView.as_view(), name= 'index'),
#/music/songs/
path ('songs/', views.SongsIndexView.as_view(), name= 'song-index'),
#/music/songs/add/
path ('songs/add/', views.AddSongFormView.as_view(), name= 'add-songs'),
#/music/3/delete
path ('songs/<int:pk>/delete/', views.DeleteSongFormView.as_view(), name= 'song-delete'),
#/music/83/
path ('<int:pk>/', views.DetailView.as_view(), name='detail'),
#/music/album/add/
path ('album/add/', views.add_album, name= 'add_album'),
#/music/album/add-comments/
path ('album/add-comments/', views.add_comments, name= 'comments'),
#/music/album/3/update/
path ('album/<int:pk>/', views.UpdateAlbumFormView.as_view(), name= 'update_album'),

] 
