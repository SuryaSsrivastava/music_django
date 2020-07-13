from django.conf.urls import url
from django.urls import path,include
from music import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'songs',views.SongViewSet)

app_name='music'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', account_view.logout, name='logout_user'),
    path('<int:album_id>/', views.detail, name='detail'),
    path('<int:song_id>/favorite/', views.favorite, name='favorite'),
    path('songs/<slug:filter_by>/', views.songs, name='songs'),
    path('create_album/', views.create_album, name='create_album'),
    path('<int:album_id>/create_song/', views.create_song, name='create_song'),
    path('<int:album_id>/delete_song/<int:song_id>/', views.delete_song, name='delete_song'),
    path('<int:album_id>/favorite_album/', views.favorite_album, name='favorite_album'),
    path('<int:album_id>/delete_album/', views.delete_album, name='delete_album'),
    path("api/",include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

