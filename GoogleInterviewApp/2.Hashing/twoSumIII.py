# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/

#Design a data structure that accepts a stream of integers and
#checks if it has a pair of integers that sum up to a particular value.

#Implement the TwoSum class:

#TwoSum() Initializes the TwoSum object, with an empty array initially.
#void add(int number) Adds number to the data structure.
#boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

#Input
#["TwoSum", "add", "add", "add", "find", "find"]
#[[], [1], [3], [5], [4], [7]]
#Output
#[null, null, null, null, true, false]
#
#Explanation
#TwoSum twoSum = new TwoSum();
#twoSum.add(1);   // [] --> [1]
#twoSum.add(3);   // [1] --> [1,3]
#twoSum.add(5);   // [1,3] --> [1,3,5]
#twoSum.find(4);  // 1 + 3 = 4, return true
#twoSum.find(7);  // No two integers sum up to 7, return false

#using HashSet
class TwoSum:
    def __init__(self):
        self.set = set()
        self.list = []

    def add(self, number: int) -> None:
        for n in self.list:
            self.set.add(number + n)
        self.list.append(number)

    def find(self, value: int) -> bool:
        return value in self.set
    
#using HashMap
class TwoSum2:
    def __init__(self) -> None:
        self.hash_map = {}

    def add(self, number: int) -> None:
        #store the quantity of numbers
        if number in self.hash_map:
            self.hash_map[number] += 1
        else:
            self.hash_map[number] = 1

    def find(self, value: int) -> bool:
        for num in self.hash_map.keys():
            sum = value - num
            if num != sum:
                if sum in self.hash_map:
                    return True
            elif self.hash_map[num] > 1:
                return True
            
        return False

obj = TwoSum()
obj.add(1)
obj.add(3)
obj.add(5)
print(obj.find(4))
print(obj.find(7))