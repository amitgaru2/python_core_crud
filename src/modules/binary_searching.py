'''
    Binary search algorithm
    Best time complexity - O(1)
    Average time complexity - O(logn)
    Worst time complexity - O(logn)
    Worst space complexity - O(1)
'''

def binary_search(result, key):
    high = len(result)-1
    low = 0
    mid = high//2

    if (high<low):        # high == mid == low in case of high=mid=low=0
        return False

    else:
        if result[mid]==key:
            return result[mid]

        elif key<result[mid]:
            return binary_search(result[low:mid], key)

        else:
            return binary_search(result[mid+1:high+1], key)
