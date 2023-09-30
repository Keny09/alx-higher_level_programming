def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: The index of a peak in the list.
    """

    # Check if the list is empty.
    if not list_of_integers:
        return None

    # Check if the list has only one element.
    if len(list_of_integers) == 1:
        return 0

    # Initialize the left and right indices.
    left = 0
    right = len(list_of_integers) - 1

    # While the left index is less than the right index, continue the search.
    while left < right:
        # Calculate the middle index.
        middle = (left + right) // 2

        # Check if the middle element is a peak.
        if list_of_integers[middle] > list_of_integers[middle - 1] and list_of_integers[middle] > list_of_integers[middle + 1]:
            return middle

        # If the middle element is not a peak, check if the left element is greater than the middle element.
        elif list_of_integers[middle - 1] > list_of_integers[middle]:
            right = middle - 1

        # Otherwise, the right element must be greater than the middle element.
        else:
            left = middle + 1

    # Return the index of the peak.
    return left