from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from music import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    #/music/album/help/
    path ('music/help/', views.album_help, name= 'album_help'),
    path ('albums/', views.AlbumList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)