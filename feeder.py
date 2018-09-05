#!/usr/bin/env python
import os
import redis
import src


def get_redis():
    REDIS_CONFIG = {
        'host': os.getenv('REDIS_HOST', 'nameredis'),
        'port': int(os.getenv('REDIS_PORT', 6379))
    }
    r = redis.Redis(**REDIS_CONFIG)
    return r


def get_services():
    FEED_SERVICES = os.getenv('FEED_SERVICES', 'FeedUsername,FeedTaskname')
    return FEED_SERVICES.split(',')


def main():
    r = get_redis()
    services = get_services()
    for service in services:
        service = getattr(src, service)
        service.feed(r)

if __name__ == '__main__':
    main()
