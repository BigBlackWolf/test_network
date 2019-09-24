from rest_framework.decorators import action
from rest_framework.response import Response

from . import services
from .serializers import FanSerializer


class LikedMixin:
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        obj = self.get_object()
        fans = services.get_fans(obj)
        if request.user in fans:
            services.remove_like(obj, request.user)
        else:
            services.add_like(obj, request.user)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data.__len__())

    @action(methods=['GET'], detail=True)
    def fans(self, request, pk=None):
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)