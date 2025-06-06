# Bubble Sort Implementation in Python
# ------------------------------------
# Bubble Sort is a simple comparison-based sorting algorithm.
# It repeatedly steps through the list, compares adjacent elements,
# and swaps them if they are in the wrong order.
# This process is repeated until the list is sorted.
#
# Time Complexity:
#   - Worst-case: O(n^2)
#   - Best-case: O(n) (when the list is already sorted, with optimization)
#   - Average-case: O(n^2)
# Space Complexity: O(1) (in-place sorting)
#
# Reasoning:
#   - Bubble Sort is called so because smaller elements "bubble" to the top
#     (beginning of the list) with each pass.
#   - After each outer loop iteration, the largest unsorted element is placed
#     at its correct position at the end of the list.
#   - It is easy to implement but inefficient for large datasets.
#
# Example Usage Cases:
#   - Educational purposes (to teach sorting concepts)
#   - Small datasets where simplicity is more important than performance
#   - Situations where memory usage must be minimal (in-place sorting)
#   - Not recommended for large or performance-critical applications


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
