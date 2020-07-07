from django.urls import path

from . import views


app_name = 'api'

urlpatterns = [
    path('videos/', views.FilterVideosView.as_view(), name='get_videos_by_tag')
]