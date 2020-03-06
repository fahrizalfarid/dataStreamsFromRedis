import redis
from datetime import datetime
from json import dumps,loads


class queue():
    def __init__(self):
        # rpush queue nya ke kanan
        # lpush queue nya ke kiri
        self.connection = redis.StrictRedis(host='localhost',port=6379, db=0)


    def currentTime(self):
        datetimeOBJ = datetime.now()
        timestamp = datetimeOBJ.strftime("%d-%b-%Y %H:%M:%S")
        return timestamp


    def setExpire(self):
        self.connection.expire("dataLidar",10800)


    def pushQueue(self, data):
        try:
            push_to_queue = self.connection.rpush("dataLidar", dumps({"timestamp":self.currentTime(),"data":data}))
            self.setExpire()
            return True
        except:
            return False



    def popQueue(self):
        try:
            pop_from_queue = self.connection.rpop("dataLidar")
            pop_from_queue = loads(pop_from_queue)

            if pop_from_queue is not None:
                return pop_from_queue['data']
            else:
                return None
        except:
            pass