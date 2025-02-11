def findMaximumSubarray(arr, low, high):
    if high == low:
        return (low, high, arr[low])
    else:
        mid = (low + high) // 2
        leftLow, leftHigh, leftSum = findMaximumSubarray(arr, low, mid)
        rightLow, rightHigh, rightSum = findMaximumSubarray(arr, mid + 1, high)
        crossLow, crossHigh, crossSum = findMaxCrossingSubarray(arr, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return (leftLow, leftHigh, leftSum)
        elif rightSum >= leftSum and rightSum >= crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)
        
def findMaxCrossingSubarray(arr, low, mid, high):
    leftSum = float('-inf')
    sum = 0
    maxLeft = -1
    for i in range(mid, low, -1):
        sum = sum + arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    rightSum = float('-inf')
    sum = 0
    maxRight = -1
    for j in range(mid+1, high):
        sum = sum + arr[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
            
    return (maxLeft, maxRight, leftSum + rightSum)

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(findMaximumSubarray(arr, 0, len(arr)-1))