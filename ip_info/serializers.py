import ipaddress
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class IpInfoSerializerRequest(serializers.Serializer):
    ip_list = serializers.ListField(child=serializers.CharField())

    @staticmethod
    def validate_ip_list(ip_list):
        for ip in ip_list:
            try:
                ipaddress.ip_address(ip)
            except ValueError:
                raise ValidationError(f"Ip address is invalid: {ip}")
        return ip_list
