cache.py
cache implemented here is cache-aside [https://codeahoy.com/2017/08/11/caching-strategies-and-how-to-choose-the-right-one/]

LRU is implemented using orderedDict because it offers queue+hash functionality i:e we can have key-value data type while maintaining the order of insertion which enable us to remove the last used item or FIFO. 

TTL : Time to live , or expiration time for a key in the cache is set to 15 seconds, all the keys are assigned a ttl and origin time , origin time is reset if the keys are accessed.expire_key() is used to check if the key has expired or not.

To implement geoligically distributed part : my idea was to make seperated cache for each region and access the cache based on the incoming IP address. In the code I have made seperate cache for 3 regions which can be stored in different servers, and can be accessed based on their IP, for simplicity I have filterd them using the first octate of the requesting IP address. Mapping of ocatate to region is given at IP_REGION 

source.py
This is the server side code to use the cache, it contains test cases to simulate requests coming from different IP address. It also shows data consistency through the caches i:e if the main db is updated all the caches will be updated as well in real time.

