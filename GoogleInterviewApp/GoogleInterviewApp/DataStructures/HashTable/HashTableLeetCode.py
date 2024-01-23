class MyHashSet:
    def __init__(self):
        self.MAX_LEN = 100000
        self.set = [None] * self.MAX_LEN

    def getIndex(self, key):
        return key % self.MAX_LEN

    def getPos(self, key, index):
        temp = self.set[index]
        if temp is None:
            return -1
        for i in range(len(temp)):
            if temp[i] == key:
                return i
        return -1

    def add(self, key):
        index = self.getIndex(key)
        pos = self.getPos(key, index)
        if pos < 0:
            if self.set[index] is None:
                self.set[index] = []
            self.set[index].append(key)

    def remove(self, key):
        index = self.getIndex(key)
        pos = self.getPos(key, index)
        if pos >= 0:
            self.set[index].remove(pos)
    
    def contains(self, key):
        index = self.getIndex(key)
        pos = self.getPos(key, index)
        return pos >= 0

class MyHashMap:
    def __init__(self):
        self.MAX_LEN = 100000
        self.map = [None] * self.MAX_LEN

    def getIndex(self, key):
        return key % self.MAX_LEN

    def getPos(self, key, index):
        temp = self.map[index]
        if temp is None:
            return -1

        for i in range(len(temp)):
            if temp[i][0] == key:
                return i
        return -1
    
    def put(self, key, value):
        index = self.getIndex(key)
        pos = self.getPos(key, index)
        if pos < 0:
            if self.map[index] is None:
                self.map[index] = []
            self.map[index].append((key, value))
        else:
            self.map[index][pos] = (key, value)

    def get(self, key):
        index = self.getIndex(key)
        pos = self.getPos(key, index)
        if pos < 0:
            return -1
        else:
            return self.map[index][pos]
        
myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
myHashSet.add(1)

print(myHashSet.getIndex(1))
print(myHashSet.getPos(1, 0))

myHashMap = MyHashMap()
myHashMap.put(1, "value1")
myHashMap.put(2, "value2")
print(myHashMap.getPos(1, 0))
print(myHashMap.getIndex(2))