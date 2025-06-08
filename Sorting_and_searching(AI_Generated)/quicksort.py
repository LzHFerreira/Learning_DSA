def quicksort(arr):
    """
    Sorts a list in ascending order using the quicksort algorithm.
    Args:
        arr: List of comparable elements (e.g., integers, floats, strings).
    Returns:
        A new sorted list (original list is not modified).
    """
    # Base case: a list of zero or one elements is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (here, we use the last element)
    pivot = arr[-1]
    left = []  # Elements less than the pivot
    right = []  # Elements greater than the pivot
    equal = []  # Elements equal to the pivot (for stability with duplicates)

    # Partition the list into left, equal, and right
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    # Recursively sort left and right, then combine
    return quicksort(left) + equal + quicksort(right)


# Example usage:
if __name__ == "__main__":
    SORTED_LIST_LABEL = "Sorted list:  "
    # Example 1: Sorting integers
    numbers = [10, 7, 8, 9, 1, 5]
    print("Original list:", numbers)
    sorted_numbers = quicksort(numbers)
    print(SORTED_LIST_LABEL, sorted_numbers)

    # Example 2: Sorting floats
    floats = [3.2, 1.5, 4.8, 2.9]
    print("\nOriginal list:", floats)
    sorted_floats = quicksort(floats)
    print(SORTED_LIST_LABEL, sorted_floats)

    # Example 3: Sorting strings (alphabetically)
    words = ["banana", "apple", "cherry", "date"]
    print("\nOriginal list:", words)
    sorted_words = quicksort(words)
    print(SORTED_LIST_LABEL, sorted_words)
