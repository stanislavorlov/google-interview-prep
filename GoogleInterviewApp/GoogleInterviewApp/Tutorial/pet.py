from collections import defaultdict


strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

res = defaultdict(list)
for str in strings:
    key = []
    for ch in str:
        key.append(ord(ch) - ord(str[0]) % 26)
    res[tuple(key)].append(str)

print(res)
print(0 % 26)   #0
print(1 % 26)   #1
print(-1 % 26)   #25