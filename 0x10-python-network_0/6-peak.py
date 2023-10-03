def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integers.
    The function uses a divide and conquer approach to find the peak.
    It has a time complexity of O(log(n)).
    """
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if list_of_integers[mid1] < list_of_integers[mid2]:
            low = mid1 + 1
        else:
            high = mid2 - 1

    return list_of_integers[low]
