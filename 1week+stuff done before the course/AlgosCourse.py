def binary_search(list, target):

    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target: 
            return midpoint -1
        
        elif list[midpoint] < target: 
            first = midpoint + 1
        else:
            last = midpoint - 1

    return 0



lst = [i for i in range(12)]



def recursive_binary_search(list, target):

    if len(list) == 0:
        return False
    
    else: 
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)

            else:
                return recursive_binary_search(list[:midpoint], target)
            




def merge_sort(list):

    """
    sort list in ascending order 
    return sorted list

    Divide: Find midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted playlists created in previous step 
    """

    if len(list) <= 1:
        return list 
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    divide the unsorted list at midpoint into sublists  
    return two sublists - left and right
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrs), sorting them in the process    
    Returns a merged list 
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right): 
        
        if left[i] < right[j]:
            l.append(left[i])
            i += 1 

        else: 
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1 
    
    while j < len(right):
        l.append(right[j])
        j += 1

    return l 




alist = [324, 2, 4, 1, 5, 6, 8, 12, 45]
l = merge_sort(alist)


def is_sorted(list):

    length = len(list)

    if length == 0 or length == 1:
        return True
    
    return list[0] < list[1] and is_sorted(list[1:])


print(is_sorted(alist))

