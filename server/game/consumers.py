import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings

class ChatConsumer(WebsocketConsumer):
    _count = 0
    def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'name1'
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self._count = settings.COUNT
        settings.COUNT += 1
        print('self count')
        print(self._count)
        print(settings.COUNT)

        self.accept()

    def disconnect(self, close_code):
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        # Redis
        settings.COUNT -= 1
        settings.DETECTIVES.pop()
        self._count = -1
        print('self count')
        print(self._count)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        
        print(message)
        if self._count >= 0:
            if len(settings.DETECTIVES) < self._count + 1:
                settings.DETECTIVES.append(message['detective'])
            else:
                settings.DETECTIVES[self._count] = message['detective']


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