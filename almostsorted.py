# Given an array of n elements, where each element is at most k away from its target position, 
# devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, 
# an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

def heap_pop(arr):
    arr[-1], arr[0] = arr[0], arr[-1]
    arr = arr[:(-1)]
    curr_pos = 0
    len_arr = len(arr)
    
    while curr_pos < len_arr:
        left_child = (curr_pos * 2) + 1
        right_child = (curr_pos * 2) + 2

        if right_child < len_arr:
            left = True if arr[left_child] < arr[right_child] else False

            if left and arr[curr_pos] > arr[left_child]:
                arr[left_child], arr[curr_pos] = arr[curr_pos], arr[left_child]
                curr_pos = left_child
            elif arr[curr_pos] > arr[right_child]:
                arr[right_child], arr[curr_pos] = arr[curr_pos], arr[right_child]
                curr_pos = right_child
        elif left_child < len_arr and arr[curr_pos] > arr[left_child]:
            arr[left_child], arr[curr_pos] = arr[curr_pos], arr[left_child]
            curr_pos = left_child
        else:
            break
    
    return arr

def heap_push(el, arr):
    arr.append(el)
    curr_pos = len(arr) - 1
    parent = (curr_pos - 1) // 2

    while parent >= 0 and arr[parent] > arr[curr_pos]:
        arr[parent], arr[curr_pos] = arr[curr_pos], arr[parent]
        curr_pos = parent
        parent = (curr_pos - 1) // 2
    
    return arr

def create_min_heap(arr):
    min_heap = []

    for num in arr:
        min_heap = heap_push(num, min_heap)
    
    return min_heap

def sort_almost_sorted(k, arr):
    k_min_heap = create_min_heap(arr[:(k+1)]) # creating min heap takes O(klog(k)) time
    new_ind = k + 1
    len_arr = len(arr)
    sorted = []

    while len(k_min_heap) > 0:      # k_min_heap is empty after we have cleared all n elements (O(n) time)
        min_num = k_min_heap[0]
        k_min_heap = heap_pop(k_min_heap)

        sorted.append(min_num)

        if new_ind < len_arr:
            heap_push(arr[new_ind], k_min_heap)     # min heap push takes O(log(k)) time - min heap stays at length <= k
            new_ind += 1
     
    # run time in total is O(nlog(k) + klog(k)) = O(nlog(k))
    return sorted

def test():
    # Example 1
    ex1 = [6, 5, 3, 2, 8, 10, 9]
    k1 = 3
    result1 = sort_almost_sorted(k1, ex1)
    print(result1)
    # expect [2, 3, 5, 6, 8, 9, 10]

    # Example 2
    ex2 = [10, 9, 8, 7, 4, 70, 60, 50]
    k2 = 4
    result2 = sort_almost_sorted(k2, ex2)
    print(result2)
    # expect [4, 7, 8, 9, 10, 50, 60, 70]

test()