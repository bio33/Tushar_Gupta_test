from collections import OrderedDict
import time


TTL = 15
IP_REGION = {
    "US":(0,80),
    "EU":(80,160),
    "CA":(160,256)
    }
class lru:
    def __init__(self,capacity,region):
        self.capacity = capacity
        self.region = region
        self.cache = OrderedDict()
        
    def get(self,key):
        if key in self.cache:
            #hit ->pop() and insert()
            val = self.cache.pop(key)
            #reset origin time
            val["origin"]=time.time()//10
            self.cache[key]=val
            return val["value"]
        else:
            # cache miss
            return None
        
    def set(self,key,value):    
        #if cache is full
        if len(self.cache) == self.capacity:
            #FIFO
            self.cache.popitem(last=False)   
        self.cache[key] = {"value":value,"ttl" : TTL,"origin":int(time.time())}

    def expire_key(self):
        print(self.cache.items())
        keys = []
        for key,val in self.cache.items():
            if int(time.time()) - val["origin"] > val["ttl"]:
                keys.append(key)
        for key in keys:
            self.cache.pop(key) 
                
    def get_region(self):
        #return cache region
        return self.region

def region_filter(ip):
    #return the region on the lru based on a given ip
    ip_octates = list(map(int,ip.split(".")))
    
    for region in IP_REGION:
        if ip_octates[0] < IP_REGION[region][1]:
            lru_region = region
            break
    return lru_region
            

    




