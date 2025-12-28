from random import choice

class RandomizedSet:

    def __init__(self):
        self.nums = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.nums: 
            self.nums.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.nums.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(list(self.nums))