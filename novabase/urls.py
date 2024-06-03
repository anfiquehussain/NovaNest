
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Novabase_home,name='home'),
    path('ytv',views.Youtube_videos_page,name='ytv'),
    path('upload_ytv',views.Upload_youtube_videos,name='upload_ytv'),
]
