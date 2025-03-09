def binary_search(arr, target, reverse=False):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif (arr[mid] < target and not reverse) or (arr[mid] > target and reverse):
            left = mid + 1
        else:
            right = mid - 1
    return -1
