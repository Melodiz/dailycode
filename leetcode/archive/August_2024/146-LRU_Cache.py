class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru_list = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_list.remove(key)
            self.lru_list.append(key)
            return self.cache[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru_list.remove(key)
        elif len(self.cache) == self.capacity:
            lru_key = self.lru_list.pop(0)
            del self.cache[lru_key]
        self.cache[key] = value
        self.lru_list.append(key)