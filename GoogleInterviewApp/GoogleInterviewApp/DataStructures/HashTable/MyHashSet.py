from itertools import combinations

class MyHashSet:

    def __init__(self) -> None:
        self.set = set()

    def add(self, key: int) -> None:
        if (self.contains(key) == False):
            self.set.add(key)

    def remove(self, key: int) -> None:
        if (self.contains(key) == True):
            self.set.remove(key)


        # from itertools import combinations

        # cardsInHand = 7
        # hands = combinations(cards,  cardsInHand)

        # n = 0
        # for h in hands:
        #     n += 1

    def contains(self, key: int) -> bool:
        for k,v in enumerate(self.set):
            if v == key:
                return True
        return False

myHashSet  = MyHashSet()
myHashSet.add(1)                   # set = [1]
myHashSet.add(2)                   # set = [1, 2]
print(myHashSet.contains(1))       # return True
print(myHashSet.contains(3))       # return False
myHashSet.add(2)                   # set = [1, 2]
print(myHashSet.contains(2))       # True
myHashSet.remove(2)                # set = [1]
print(myHashSet.contains(2))       # False




def containsDuplicate(nums: list[int]) -> bool: # type: ignore
    mySet = set()
    for _, num in enumerate(nums): # type: ignore
        if num not in mySet:
            mySet.add(num)
        else:
            return True
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))