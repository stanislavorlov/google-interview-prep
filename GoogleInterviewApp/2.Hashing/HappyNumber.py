# A happy number is a number defined by the following process:
#   Starting with any positive integer, replace the number by the sum of the squares of its digits.
#   Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#   Those numbers for which this process ends in 1 are happy.

class Solution:
    def isHappy(self, n:int) -> bool:
        cache = set([])
        
        while True:
            new_number = 0
            
            while n > 0:
                new_number += (n % 10)**2
                n //= 10
            
            if new_number in cache:
                return False
            
            cache.add(new_number)

            if new_number == 1:
                return True

            n = new_number

solution = Solution()
solution.isHappy(2)