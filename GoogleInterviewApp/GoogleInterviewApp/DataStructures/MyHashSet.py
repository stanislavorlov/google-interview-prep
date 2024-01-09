from pickle import TRUE


class MyHashSet:

    def __init__(self) -> None:
        self.set = []

    def add(self, key: int) -> None:
        self.set.append(key)

    def remove(self, key: int) -> None:
        self.set.remove(key)

    def contains(self, key: int) -> bool:
        for k,v in enumerate(self.set):
            if v == key:
                return True
        return False

key = 3    
obj = MyHashSet()
obj.add(key)
obj.remove(key)
contains = obj.contains(key)

print(contains)