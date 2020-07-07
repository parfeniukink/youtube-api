from django.test import TestCase

from .models import Channel, Video, Performance, Stat, Tag
from .forms import ChannelIdForm, TagsForm

from app.services import filter


class ProjectTests(TestCase):
    def setUp(self):
        self.channel = Channel.objects.create(chan_id="UC2WHjPDvbE6O328n17ZGcfg",
                                              title="ForrestKnight",
                                              description="Channel description")
        self.video_1 = Video.objects.create(channel=self.channel,
                                            video_id="jfxcJH_OWgE",
                                            title="jfxcJH_OWgE title",
                                            description="jfxcJH_OWgE description")
        self.video_2 = Video.objects.create(channel=self.channel,
                                            video_id="xa6me8wou_k",
                                            title="xa6me8wou_k title",
                                            description="xa6me8wou_k description")
        self.stat_1 = Stat.objects.create(video=self.video_1,
                                          key="views",
                                          value="199")
        self.stat_2 = Stat.objects.create(video=self.video_2,
                                          key="views",
                                          value="388")
        self.performance_1 = Performance.objects.create(video=self.video_1,
                                                        key="definition",
                                                        value="hd")
        self.performance_2 = Performance.objects.create(video=self.video_2,
                                                        key="definition",
                                                        value="fhd")
        self.tag_coding = Tag.objects.create(tag="coding")
        self.tag_programming = Tag.objects.create(tag="programming")

        self.video_1.tags.add(self.tag_coding)
        self.video_2.tags.add(self.tag_programming)

    def test_channel(self):
        print("test_channel")
        channel = Channel.objects.get(chan_id='UC2WHjPDvbE6O328n17ZGcfg')

        self.assertEqual(channel, self.channel)

    def test_videos(self):
        print('test_videos')
        test_video_1 = Video.objects.get(video_id='jfxcJH_OWgE')
        test_video_2 = Video.objects.get(video_id='xa6me8wou_k')

        self.assertEqual(test_video_1, self.video_1)
        self.assertEqual(test_video_2, self.video_2)

    def test_video_stats(self):
        print('test_video_stats')
        test_video_1_stats = Stat.objects.get(video=self.video_1)
        test_video_2_stats = Stat.objects.get(video=self.video_2)

        self.assertEqual(test_video_1_stats, self.stat_1)
        self.assertEqual(test_video_2_stats, self.stat_2)

    def test_video_performances(self):
        print('test_video_performances')
        test_video_1_performances = Performance.objects.get(video=self.video_1)
        test_video_2_performances = Performance.objects.get(video=self.video_2)

        self.assertEqual(test_video_1_performances, self.performance_1)
        self.assertEqual(test_video_2_performances, self.performance_2)

    def test_tags(self):
        print('test_tags')
        test_tag_1 = Tag.objects.get(tag='coding')
        test_tag_2 = Tag.objects.get(tag='programming')
        self.assertEqual(test_tag_1, self.tag_coding)
        self.assertEqual(test_tag_2, self.tag_programming)

    def test_video_tags(self):
        print('test_video_tags')
        test_video_1 = Video.objects.get(video_id='jfxcJH_OWgE')
        test_video_2 = Video.objects.get(video_id='xa6me8wou_k')

        self.assertEqual(test_video_1.tags.all()[0], self.tag_coding)
        self.assertEqual(test_video_2.tags.all()[0], self.tag_programming)

    ################################################
    ####    Testing Views   ####
    ################################################
    def test_homepage_get(self):
        print('test_homepage')
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_channel_post(self):
        print('test_channel_post')
        clean_data = {
            "channel_id": "UC2WHjPDvbE6O328n17ZGcfg"
        }
        wrong_data = {
            "channel": "UC2WHjPDvbE6O"
        }
        response_1 = self.client.post('/',
                                      data=clean_data)
        response_2 = self.client.post('/',
                                      data=wrong_data)
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)

    def test_chanel_id_form(self):
        print('test_chanel_id_form')
        clean_form_data = {"channel_id": 'UC2WHjPDvbE6O328n17ZGcfg'}
        wrong_form_data = {"channel_id": '6O328n17ZGcfg'}
        none_form_data = {"channel_id": ''}
        clean_form = ChannelIdForm(data=clean_form_data)
        wrong_form = ChannelIdForm(data=wrong_form_data)
        none_form = ChannelIdForm(data=none_form_data)

        self.assertTrue(clean_form.is_valid())
        self.assertFalse(wrong_form.is_valid())
        self.assertFalse(none_form.is_valid())

    def test_tags_form(self):
        print('test_tags_form')
        clean_form_data = {"tags": 'coding'}
        wrong_form_data = {"tags": ''}
        clean_form = TagsForm(data=clean_form_data)
        wrong_form = TagsForm(data=wrong_form_data)

        self.assertTrue(clean_form.is_valid())
        self.assertFalse(wrong_form.is_valid())

    def test_tag_filter(self):
        print('test_video_tags')
        clean_tags = "coding, programming"
        clean_tag_1 = "coding"
        clean_tag_2 = "programming"
        wrong_tag = 'tag'

        test_videos = filter.get_videos_by_tags(clean_tags)
        test_video_1 = filter.get_videos_by_tags(clean_tag_1)
        test_video_2 = filter.get_videos_by_tags(clean_tag_2)
        test_no_videos = filter.get_videos_by_tags(wrong_tag)

        videos = Video.objects.all()

        self.assertEqual(test_no_videos, None)
        self.assertEqual(test_video_1[0], self.video_1)
        self.assertEqual(test_video_2[0], self.video_2)
        self.assertEqual(list(test_videos), list(videos))

