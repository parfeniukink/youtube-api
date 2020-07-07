from django.db import models


class Channel(models.Model):
    chan_id = models.CharField(max_length=24, null=False)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=True)


class Video(models.Model):
    channel = models.ForeignKey(Channel,
                                on_delete=models.CASCADE,
                                related_name='videos')
    video_id = models.CharField(max_length=11, null=False)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=True)


class Stat(models.Model):
    video = models.ForeignKey(Video,
                              on_delete=models.CASCADE,
                              related_name='stats')
    key = models.CharField(max_length=50, null=False)
    value = models.CharField(max_length=100, null=False)


class Performance(models.Model):
    video = models.ForeignKey(Video,
                              on_delete=models.CASCADE,
                              related_name='performances',
                              related_query_name='performance')
    key = models.CharField(max_length=50, null=False)
    value = models.CharField(max_length=100, null=False)


class Tag(models.Model):
    tag = models.CharField(max_length=50, null=False)
    video = models.ManyToManyField('Video',
                                   related_name='tags',
                                   related_query_name='tag')