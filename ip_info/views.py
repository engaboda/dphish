from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import IpInfoSerializerRequest
from .tasks import get_ip_info


class IpAddressViewSet(viewsets.ViewSet):
    serializer_class = IpInfoSerializerRequest

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_ip_info.delay(serializer.data.get('ip_list'), 1234)
        return Response({"message": "working on your request."})
