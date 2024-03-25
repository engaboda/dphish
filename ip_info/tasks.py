import json
from websocket import create_connection
import logging
import ipinfo
from celery import shared_task
from django.conf import settings

logger = logging.getLogger(__name__)
handler = ipinfo.getHandler(settings.IP_INFO_ACCESS_TOKEN)


def post_ip_info_to_channel(ip_addresses_details, client_id):
    websocket = create_connection(f"ws://{settings.HOST}:8000/ws/notification/{client_id}/")
    websocket.send(json.dumps({"message": ip_addresses_details}))
    websocket.recv()
    websocket.close()


@shared_task
def get_ip_info(ip_addresses, client_id):
    details = handler.getBatchDetails(ip_addresses)
    logger.info(f"<Info> {details}")
    post_ip_info_to_channel(details, client_id)
    return details
