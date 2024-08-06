import unittest

def merge_sort(arr):
    if len(arr) < 2:
        return
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    merge_sort(left_arr)
    merge_sort(right_arr)
    
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
        
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
        
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

class TestMethods(unittest.TestCase):
    
    def test_sort(self):
        arr = [12, 7, 5, 13, 6, 11]
        merge_sort(arr)

        self.assertEqual(arr, [5,6,7,11,12,13])

unittest.main()