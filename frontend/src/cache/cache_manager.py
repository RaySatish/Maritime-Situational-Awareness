from redis import Redis

class CacheManager:
    def __init__(self):
        self.redis_client = Redis(host='localhost', port=6379)
