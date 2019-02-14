from cache import lru,region_filter
import time
TEMP_DB = {
     1 : "random text data",
     2 : "not so random random text",
     3 : "predictable random text",
     4 : "I got unimaginative in my plum test"
}

CACHE_CAPACITY = 3
caches = {}

def get_cache(reg):
    if reg in caches:
        cache = caches[reg]
    else:
        caches[reg] = lru(CACHE_CAPACITY,reg)
        cache = caches[reg]
    return cache


# access cache based on ip
def access_data(ip,key):
    # get the region based on IP
    reg = region_filter(ip)    
    # get the cache based on region
    lru_cache = get_cache(reg)
    # access cacahe
    val = lru_cache.get(key)
    # cache miss , add the value to cache
    if val == None :
        lru_cache.set(key,TEMP_DB[key])
        val = lru_cache.get(key)
    return val

def update_caches(key,value):
    for cache,cache_obj in caches.items():
        if key in cache_obj.cache:  
            cache_obj.cache[key]["value"] = value

# updated db and all the caches conating the new value
def update_db(key,value):
    if key in TEMP_DB:
        TEMP_DB[key] = value
    else:
        TEMP_DB[key] = value

    update_caches(key,value)

#util function
def print_caches():
    for cache in caches:
        print(cache,": ",caches[cache].cache)
def tc1():
    '''
    IP_REGION = {
    "US":(0,80),
    "EU":(80,160),
    "CA":(160,256)
        }
    '''
    # create and access cache in CA
    print(access_data("212.12.12.12",2))
    # create and access cache in EU
    print(access_data("112.1.1.2",1))
    # update TEMP_DB using update_db only
    update_db(2,"hello world")
    # access the cache to verify updated values
    print(access_data("212.12.12.12",2))
    print(access_data("112.1.1.2",2))

def tc2():
    # get data in cache
    access_data("2.3.2.1",1)
    print_caches()
    print("waiting for key to expire")
    time.sleep(5)
    for cache in caches:
        print(cache)
        caches[cache].expire_key()
    print_caches()

def tc3():
    us_ip = "23.12.3.12"
    eu_ip = "123.12.31.32"
    ca_ip = "200.12.32.12"
    print("accessing US cache : ",access_data(us_ip,1)) 
    print("accessing EU cache : ",access_data(eu_ip,2))
    print("accessing CA cache : ",access_data(ca_ip,3))
    

if __name__ == "__main__":
    # testcase 1 : data consistency
    tc1()
    # testcase 2 : data expiration 
    tc2()
    # testcase 3 : location based caches
    tc3()

