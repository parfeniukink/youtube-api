from celery import shared_task

from .services import youtube, repo


@shared_task
def scrap_channel(*args, **kwargs):
    if kwargs:
        channel_id = kwargs['channel_id']
        channel_info = youtube.get_channel_info(channel_id)
        channel = repo.channel_save(channel_id=channel_id, channel_info=channel_info)

        channel_videos = youtube.get_channel_videos(channel_id)
        for channel_video in channel_videos:
            print('-' * 20)
            print(channel_video.id, 'is updated')
            video, video_created = repo.video_save(channel_video, channel)
            stats = youtube.get_video_stats(channel_video.id)
            repo.video_info_save(stats=stats, video=video, video_created=video_created)

