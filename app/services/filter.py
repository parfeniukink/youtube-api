from app import models


def get_videos_by_tags(str_tags: str):
    if str_tags:
        tags = [i.strip() for i in str_tags.split(',')]
        tag_set = models.Tag.objects.filter(tag__in=tags)
        videos = models.Video.objects.filter(tag__in=tag_set)
        if len(videos) == 0:
            return None
        return videos
