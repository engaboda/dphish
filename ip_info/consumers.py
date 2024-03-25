import logging
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

logger = logging.getLogger(__name__)


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.client_id = self.scope["url_route"]["kwargs"]["client_id"]
        self.client_group_name = f"chat_{self.client_id}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.client_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.client_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        for ip, info in message.items():
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.client_group_name, {"type": "notification.message", "message": {ip: info}}
            )

    # Receive message from client group
    def notification_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
