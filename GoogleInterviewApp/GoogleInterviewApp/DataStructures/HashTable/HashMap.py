class HashMap(object):
    def __init__(self, size):
        self.data = [[]] * size

    def hash(self, param, size):
        hash_value = 0
        for i in range(len(param)):
            hash_value = (hash_value + ord(param[i]) * i) % size

        return hash_value
    
    def set(self, key, value):
        address = self.hash(key, len(self.data))

        if not self.data[address]:
            self.data[address] = []

        # in case of too many values, those values can be maintained in a balanced binary search tree
        self.data[address].append([key,value])

        return self.data
    
    def get(self, key):
        output = []
        address = self.hash(key, len(self.data))
        currentBucket = self.data[address]

        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    output.append(currentBucket[i][1])
                
        return output
    
    def print(self):
        print("".join(str(item) for item in self.data))

myHashMap = HashMap(50)
myHashMap.set("key", "value")
myHashMap.set("key", "value1")
myHashMap.set("123", "456")

myHashMap.print()

print(myHashMap.get('key'))