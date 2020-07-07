from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import VideoSerializer

from app.services import filter


class FilterVideosView(APIView):
    """
        We can use body in GET <RFC 7230-7237>
        https://tools.ietf.org/html/rfc7231#section-4.3.1
    """

    def get(self, request):
        if 'tags' in request.data:
            tags = request.data.get('tags')
            videos = filter.get_videos_by_tags(tags)
            print(videos)
            serializer = VideoSerializer(videos,
                                         many=True)

            return Response(serializer.data)

        return Response({
            'Use get with body: {"tags": "coding, how to start coding"}'
        })
