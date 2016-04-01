import redis

DB = redis.StrictRedis(host='localhost', port=6379, db=1)

