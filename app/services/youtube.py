import requests

from django.conf import settings

from collections import namedtuple


def get_channel_info(channel_id, *args, **kwargs) -> dict:
    url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {'part': 'snippet',
              'id': channel_id,
              'key': settings.YOUTUBE_DATA_API_KEY}

    response = requests.get(url=url, params=params)
    channel_title = response.json()['items'][0]['snippet']['title']
    channel_description = response.json()['items'][0]['snippet']['description']
    return {'channel_title': channel_title,
            'channel_description': channel_description}


def get_channel_videos(channel_id, *args, **kwargs) -> list:
    url = 'https://www.googleapis.com/youtube/v3/search'
    video_params = {'part': 'snippet',
                    'channelId': channel_id,
                    'kind': 'youtube#video',
                    'type': 'video',
                    'videoType': 'any',
                    'maxResults': 50,
                    'key': settings.YOUTUBE_DATA_API_KEY}

    response = requests.get(url=url, params=video_params)
    response_videos = response.json()['items']
    videos = []
    for i, item in enumerate(response_videos):
        Video = namedtuple('Video', 'id, title, description')
        video = Video(id=item['id']['videoId'],
                      title=item['snippet']['title'],
                      description=item['snippet']['description'])
        videos.append(video)

    return videos


def get_video_stats(video_id: str or None, *args, **kwargs) -> dict:
    url = 'https://www.googleapis.com/youtube/v3/videos'
    video_params = {'part': 'snippet, statistics, contentDetails',
                    'id': video_id,
                    'key': settings.YOUTUBE_DATA_API_KEY}

    response = requests.get(url=url, params=video_params)
    response_snippet = response.json()['items'][0]['snippet']
    response_stats = response.json()['items'][0]['statistics']
    response_content_details = response.json()['items'][0]['contentDetails']
    tags = None
    if 'tags' in response_snippet:
        tags = response_snippet['tags']

    return {'views': response_stats['viewCount'],
            'likes': response_stats['likeCount'],
            'dislikes': response_stats['dislikeCount'],
            'comments': response_stats['commentCount'],
            'definition': response_content_details['definition'],
            'tags': tags}


