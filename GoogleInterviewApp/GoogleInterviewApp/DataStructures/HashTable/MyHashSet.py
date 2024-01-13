from itertools import combinations
from re import L

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

# return true if any value appears at least twice in the array
def containsDuplicate(nums: list[int]) -> bool: # type: ignore
    mySet = set()
    for _, num in enumerate(nums): # type: ignore
        if num not in mySet:
            mySet.add(num)
        else:
            return True
    return False

# every element appears twice except for one. Find that single one.
def singleNumber(nums: list[int]) -> int:
        dist = set()
        for _, num in enumerate(nums):
            if num not in dist:
                dist.add(num)
            else:
                dist.remove(num)
        
        return dist.pop()

nums = [1]
print(singleNumber(nums))

