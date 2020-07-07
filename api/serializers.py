from rest_framework import serializers

from app.models import Performance, Tag, Video, Channel, Stat


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ('key', 'value')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ('key', 'value')


class VideoSerializer(serializers.ModelSerializer):
    channel = serializers.SerializerMethodField()
    performance = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    @staticmethod
    def get_channel(obj):
        return ChannelSerializer(obj.channel).data

    @staticmethod
    def get_performance(obj):
        return PerformanceSerializer(obj.performances,
                                     many=True).data

    @staticmethod
    def get_tags(obj):
        return TagSerializer(obj.tags.all(),
                             many=True).data

    @staticmethod
    def get_stats(obj):
        return StatSerializer(obj.stats,
                              many=True).data

    class Meta:
        model = Video
        fields = '__all__'
        # exclude = ('channel', )
