arr = [12, 35, 1, 10, 34, 1]

def second_largest(arr): 
    first = second = -2147483648

    for n in arr:
        if n > first:
            second = first
            first = n
        else:
            if n > second:
                second = n

    return second

print(second_largest(arr))