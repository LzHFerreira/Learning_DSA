def bubble_sort(arr):
    """
    Sorts a list in ascending order using the bubble sort algorithm.
    Args:
        arr: List of comparable elements (e.g., integers, floats).
    Returns:
        None (the list is sorted in place).
    """
    n = len(arr)  # Get the length of the list
    # Outer loop: controls the number of passes
    for i in range(n):
        swapped = False  # Optimization: track if any swaps occurred in this pass
        # Inner loop: compare adjacent elements
        for j in range(0, n - i - 1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True  # Mark that a swap occurred
        # If no swaps occurred in this pass, the list is already sorted
        if not swapped:
            break  # Exit early for best-case O(n) performance


# Example usage:
if __name__ == "__main__":
    SORTED_LIST_LABEL = "Sorted list:  "
    # Example 1: Sorting integers
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", numbers)
    bubble_sort(numbers)
    print(SORTED_LIST_LABEL, numbers)

    # Example 2: Sorting floats
    floats = [3.2, 1.5, 4.8, 2.9]
    print("\nOriginal list:", floats)
    bubble_sort(floats)
    print(SORTED_LIST_LABEL, floats)

    # Example 3: Sorting strings (alphabetically)
    words = ["banana", "apple", "cherry", "date"]
    print("\nOriginal list:", words)
    bubble_sort(words)
    print(SORTED_LIST_LABEL, words)
