from app.models import Channel, Video, Stat, Performance, Tag
from django.db.models import F


def channel_save(channel_id: str, channel_info: dict, *args, **kwargs) -> object:
    object, created = Channel.objects.get_or_create(chan_id=channel_id)
    object.title = channel_info['channel_title']
    object.description = channel_info['channel_description']
    object.save()

    return object


def video_save(channel_video, channel, *args, **kwargs) -> object:
    object, created = Video.objects.get_or_create(channel=channel, video_id=channel_video.id)
    object.title = channel_video.title
    object.description = channel_video.description
    object.channel = channel
    object.save()

    return object, created


def video_info_save(stats: dict, video, video_created: bool, *args, **kwargs):
    for key in stats:
        if key != 'tags' and key != 'definition':
            stat, stat_created = Stat.objects.get_or_create(video=video,
                                                       key=key)
            stat.value = stats.get(key)
            stat.save()

    if video_created:
        performance, performance_created = Performance.objects.get_or_create(video=video,
                                                                             key='definition')
        performance.value = stats.get('definition')
        performance.save()

    tags = stats.get('tags')
    if video_created and tags:
        for ttag in tags:
            tag, tag_created = Tag.objects.get_or_create(tag=ttag)
            video.tags.add(tag)
            video.save()


def get_channels():
    return Channel.objects.all()
