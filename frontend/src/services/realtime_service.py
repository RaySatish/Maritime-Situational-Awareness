import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class MaritimeUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def update_vessel_position(self, data):
        await self.send(json.dumps({
            'type': 'vessel_update',
            'data': data
        }))
