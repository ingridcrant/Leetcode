from collections import deque

def median(nums1, nums2):
    # implementation in O(m+n), where m is the size of arr1 and n is the size of arr2
    # equivalent to last invocation of merge sort

    end1 = len(nums1)
    end2 = len(nums2)
    new_arr = []
    
    i = 0
    j = 0
    
    while i < end1 and j < end2:
        if nums1[i] <= nums2[j]:
            new_arr.append(nums1[i])
            i += 1
        else:
            new_arr.append(nums2[j])
            j += 1
    
    if i < end1:
        new_arr += nums1[i:]
    if j < end2:
        new_arr += nums2[j:]
    
    total_len = end1 + end2
    if total_len % 2 == 0:
        median = (new_arr[(total_len//2)-1] + new_arr[total_len//2])/2
    else:
        median = new_arr[total_len//2]
    
    return median
