hashmap = {0 : 0, 2 : 3}
print(hashmap)
print(hashmap[2])

hashmap[1] = 1
print(hashmap[1])

del hashmap[2]
print(hashmap)

if 2 not in hashmap:
    print("Key 2 is not in the hash map.")

print("The size of hash map is: " + str(len(hashmap)))

for key in hashmap:
    print(key)

print(hashmap.keys())

hashmap.clear()