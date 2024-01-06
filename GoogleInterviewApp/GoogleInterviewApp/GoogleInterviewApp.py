# def print_items(n):
#     for i in range(n):          # O(n)
#         print(i)

#     for j in range(n):          # O(n)
#         print(j)

#                                 # O(2n) = O(n) drop constants

# print_items(10)

 
def print_items(n):                #O(n^2)
    for i in range(n):
        for j in range(n):
            print(i, j)
      
        
# DO NOT CHANGE THIS LINE:
# print_items(10)
            
def add_items(n):
    return n + n + n        # O(1)


def print_items_2(a,b):
    for i in range(a):
        print(i)

    for j in range(b):          # O(a+b)
        print(j)



def print_items_3(a,b):
    for i in range(a):
        for j in range(b):          # O(a*b)
            print(i, j)


my_list = [11,3,27,2]
print(my_list)

my_list.append(15)
print(my_list)

my_list.pop()
print(my_list)

#adding at the end O(1)         adding one item
#adding at the beggining O(n)   reindexing all of items
#adding at the middle O(n)      reidexing half of items, constant drop


num1 = 11
num2 = num1

print(id(num1))         #address in memory
print(id(num2))

num2 = 22

print(id(num1))
print(id(num2))

dict1 = { 'value': 11 }

print(dict1['value'])

dict2 = dict1
dict2['value'] = 22

print(dict1)
print(dict2)