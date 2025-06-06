# Insertion Sort Implementation in Python
# --------------------------------------
# Insertion Sort is a simple, intuitive sorting algorithm.
# It builds the sorted list one element at a time by repeatedly taking the next
# unsorted element and inserting it into its correct position among the sorted elements.
#
# Time Complexity:
#   - Worst-case: O(n^2) (when the list is reverse sorted)
#   - Best-case: O(n) (when the list is already sorted)
#   - Average-case: O(n^2)
# Space Complexity: O(1) (in-place sorting)
#
# Reasoning:
#   - Insertion Sort works similarly to how you might sort playing cards in your hand.
#   - It is efficient for small datasets and nearly sorted lists.
#   - It is stable (does not change the relative order of equal elements).
#   - It is adaptive (runs faster on nearly sorted data).
#
# Example Usage Cases:
#   - Small datasets where simplicity is more important than performance
#   - Nearly sorted lists (adaptive behavior)
#   - Online sorting (can sort as new elements arrive)
#   - Useful as part of more complex algorithms (e.g., hybrid sorts like TimSort)


def insertion_sort(arr):
    """
    Sorts a list in ascending order using the insertion sort algorithm.
    Args:
        arr: List of comparable elements (e.g., integers, floats, strings).
    Returns:
        None (the list is sorted in place).
    """
    # Start from the second element (index 1) and go through the list
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted into the sorted portion
        j = i - 1  # Start comparing with the element just before key

        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element rightward
            j -= 1  # Move to the previous element

        arr[j + 1] = key  # Insert the key at the correct position


# Example usage:
if __name__ == "__main__":
    SORTED_LIST_LABEL = "Sorted list:  "
    # Example 1: Sorting integers
    numbers = [12, 11, 13, 5, 6]
    print("Original list:", numbers)
    insertion_sort(numbers)
    print(SORTED_LIST_LABEL, numbers)

    # Example 2: Sorting floats
    floats = [3.2, 1.5, 4.8, 2.9]
    print("\nOriginal list:", floats)
    insertion_sort(floats)
    print(SORTED_LIST_LABEL, floats)

    # Example 3: Sorting strings (alphabetically)
    words = ["banana", "apple", "cherry", "date"]
    print("\nOriginal list:", words)
    insertion_sort(words)
    print(SORTED_LIST_LABEL, words)
