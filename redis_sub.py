import os
import redis
import json
import time
from multiprocessing import Process
from formatPrintout import testPrint, formatDocument

print("STARTED REDIS CON, SCRIPT")
print("SLEEPING FOR 15 SECONDS TO ALLOW INTERNET CONNECTION")
# time.sleep(15)
redis_conn = redis.Redis(  host= 'redis-15456.c62.us-east-1-4.ec2.cloud.redislabs.com',
  port= '15456',
  password= 'TduKRzZYDhePnQvIb62w1lrZ6xLekzX6',charset="utf-8", decode_responses=True)


def sub(name: str):
    print("subscribing")
    pubsub = redis_conn.pubsub()
    pubsub.subscribe("broadcast")
    for message in pubsub.listen():
        try:
            print(message)
            if (type(message["data"]) == dict):
                data = json.loads(message["data"])
                print("Recieved data" , data)
                formatDocument(data)
            else:
                print("Made Connection With Redis Pubsub")
            # print("%s : %s" % (name, data))
        except Exception as e:
            print("Got exception while trying to print ")
            print(e)



if __name__ == "__main__":
   testPrint()
   sub("")
#    Process(target=sub, args=("reader1",)).start()