def binary_search_int(nums:list[int], target:int):
    #The most basic binary search to find a speficic integer value in a list of integers. 
    #Returns the index of found target, or -1 is target isnt in the list    
    left = 0
    right = len(nums)-1

    while(left<=right):
        mid = (left+right)//2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] < target):
            left = mid+1
        elif (nums[mid] > target):
            right = mid-1
    
    return -1

def binary_search_sqrt(x:int):
    #Binary search to find root of x, rounded down to the nearest positive integer.
    # Constrains: 0 <= x <= 2^31 - 1
    left = 1
    right = x
    if (x<=1): return 1           #in case x=0 or 1, loop while wont even start, so then just return 1
    while(left <= right):
        mid = (left+right)//2
        if (mid*mid == x):
            return mid
        elif (mid*mid < x):
            left = mid+1
        elif (mid*mid > x):
            right = mid-1
    if (mid*mid > x): return mid-1
    else : return mid


def binary_search_rotated_array(nums, target):
    #https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
    left = 0
    right = len(nums)-1
    while (left <= right):
        mid = (left+right)//2
        if (nums[mid] == target):
            return mid
        if(nums[left] <= nums[mid]):             #Lewa czesc jest posortowana
            if (nums[left] <= target < nums[mid]):               #target jest gdzies w <left, mid>
                right = mid-1
            else:                                   #target nie jest w posortowanej czesci -> idziemy do nieposortowanej
                left = mid+1
        else:                                   #Prawa czesc jest posortowana
            if (nums[mid] < target <= nums[right]):     #target jest w tej czesci
                left = mid+1
            else:
                right = mid-1
    return -1
