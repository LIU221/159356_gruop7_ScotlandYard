import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings

class ChatConsumerx(WebsocketConsumer):
    def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'name1'
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        # Redis
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        
        print(message)
        message['count'] = settings.COUNT
        message['detectives'] = settings.DETECTIVES
        # self.send(text_data=text_data)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        print(message)

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))