from django import forms


class ChannelIdForm(forms.Form):
    channel_id = forms.CharField(max_length=24)

    def clean_channel_id(self, *args, **kwargs):
        channel_id = self.cleaned_data['channel_id']
        if len(channel_id) != 24:
            raise forms.ValidationError("Wrong Channel ID")
        return channel_id


class TagsForm(forms.Form):
    tags = forms.CharField(max_length=300)

