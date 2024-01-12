# https://www.askpython.com/python/examples/hashmaps-in-python

class MyHashMap:

    def __init__(self):
        self.map = [[]]

    # if key already exists, update corresponding value
    def put(self, key: int, value: int) -> None:
        if self.map[key]:
            self.map[key] = [key,value]
        self.map[key].append([key,value])

    # returns -1 if no mapping for key
    def get(self, key: int) -> int:
        value = self.map[key]
        
    
    # removes the mapping if contains key
    def remove(self, key: int) -> None:
        if (self.map.keys().__contains__(key)):
            self.map.pop(key)
    
obj = MyHashMap()
obj.put(1,2)
param_2 = obj.get(1)
obj.remove(1)