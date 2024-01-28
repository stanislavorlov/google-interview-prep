import collections
nums = [9,4,9,8,4]
counter = collections.Counter(nums)
print(counter)                      #Counter({9: 2, 4: 2, 8: 1})
print(counter.keys())               #dict_keys([9, 4, 8])
print(list(counter.elements()))     #[9, 9, 4, 4, 8]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
counter12 = collections.Counter(nums1) & collections.Counter(nums2)
print(counter12)                    #Counter({4: 1, 9: 1})

intercept = set()

pattern = "abba"
s = "dog cat cat dog"
for word, p in zip(s.split(), pattern):
    print(word, p)      # dog a     cat b       cat b       dog a

l = [1,2,3,4]
for i,n in enumerate(l):
    print(i, n)    #0 1     1 2     2 3     3 4

for i in range(len(l)):
    print(i, l[i])  #0 1     1 2     2 3     3 4

dict = collections.defaultdict(int)
dict['message'] = 1