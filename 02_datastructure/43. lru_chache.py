# Implement an LRU Cache in Python

# get(key) → return the value if present, otherwise -1
# put(key, value) → insert/update a value
# When the cache exceeds its capacity, remove the least recently used item

#from collections import OrderedDict
# class LRUCache:
#      def __init__(self, capacity: int):
#          self.capacity = capacity
#          self.cache: OrderedDict[int, object] = OrderedDict()

#      def get(self, key: int):
#         if key not in self.cache:
#             return -1

# #         # Mark as recently used
#         self.cache.move_to_end(key)
#         return self.cache[key]

#      def put(self, key: int, value: str):
#         if key in self.cache:
#              # Remove old position
#              self.cache.move_to_end(key)

#         self.cache[key] = value

# #         # Remove least recently used
#         if len(self.cache) > self.capacity:
#              self.cache.popitem(last=False)
        

# lrucache = LRUCache(2)
# lrucache.put(1, "A")
# lrucache.put(2, "B")
# lrucache.get(1)
# lrucache.put(3, "C")
# lrucache.get(2)




#cache = ordereddict
#define its capacity - 2
#put 1st 
# put
# put
# if len(cache) > capcity
# popitem(last=False)
# get - move_to_end(key)
# key not in cache return -1

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache : OrderedDict[int, str] = OrderedDict()

    def put(self, key: int, value: str):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key:int):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    


lru = LRUCache(2)
lru.put(1, 'A')
lru.put(2, 'B')
print(lru)
print(lru.get(2))
lru.put(2, 'C')
print(lru.get(2))