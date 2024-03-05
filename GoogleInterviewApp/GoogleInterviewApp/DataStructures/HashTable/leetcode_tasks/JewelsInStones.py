#All the characters of jewels are unique.
# calculate number of jewels in stones
# Letters are case sensitive

#Input: jewels = "aA", stones = "aAAbbbb"
#Output: 3

#Input: jewels = "z", stones = "ZZ"
#Output: 0

def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelsSet = set(jewels)
    qty = 0
    for ch in stones:
        if ch in jewelsSet:
            qty += 1

    return qty

def jewelsOptimized(jewels: str, stones: str) -> int:
    jewelsSet = set(jewels)
    return sum(s in jewelsSet for s in stones)

print(numJewelsInStones("aA", "aAAbbbb"))   #3
print(numJewelsInStones("z", "ZZ"))         #0

