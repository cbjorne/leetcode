# Combination of map and array allows this to be possible. Index_map stores the value and the position in the array
# at that value. Remove swaps the last value with the value to be removed, then pops the last value O(1) for all ops

import random

class RandomizedSet(object):
    def __init__(self):
        self.index_map = {}
        self.values = []


    def insert(self, val):
        if val in self.index_map:
            return False
        else:
            self.index_map[val] = len(self.values)
            self.values.append(val)
            return True
        

    def remove(self, val):
        if val not in self.index_map:
            return False
        else:
            idx = self.index_map[val]
            last = self.values[-1]
            self.values[idx] = last
            self.index_map[last] = idx
            self.values.pop()
            del self.index_map[val]
            return True
        

    def getRandom(self):
        return random.choice(self.values)
        

def main():
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.insert(2))
    print(obj.remove(2))
    print(obj.getRandom())

main()
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()