import redis
import json
REDIS_HOST = 'redis-15456.c62.us-east-1-4.ec2.cloud.redislabs.com'
redis_conn = redis.Redis(  host= 'redis-15456.c62.us-east-1-4.ec2.cloud.redislabs.com',
  port= '15456',
  password= 'TduKRzZYDhePnQvIb62w1lrZ6xLekzX6',charset="utf-8", decode_responses=True)

# print(redis_conn.keys())
userNameQuery = "C"
for key in redis_conn.keys():

    try:
        data = json.loads(redis_conn.get(key))
        print(data)
        if (data["userName"] == userNameQuery):
            print(data)
    except Exception as e:
        # print(e)
        pass