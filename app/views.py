from django.shortcuts import render, redirect

from .services import repo, filter
from .forms import ChannelIdForm, TagsForm
from .tasks import scrap_channel


def index(request):
    ctx = {}
    channel_form = ChannelIdForm(request.POST or None)
    tags_form = TagsForm(request.POST or None)

    if channel_form.is_valid():
        channel_id = channel_form.data.get('channel_id')
        scrap_channel.delay(channel_id=channel_id)

    if tags_form.is_valid():
        videos = filter.get_videos_by_tags(tags_form.cleaned_data['tags'])
        if not videos:
            return redirect('app:index')
        ctx['videos'] = videos

    ctx['channels'] = repo.get_channels()
    ctx['channel_form'] = channel_form
    ctx['tags_form'] = tags_form

    return render(request=request,
                  template_name='index.html',
                  context=ctx)
