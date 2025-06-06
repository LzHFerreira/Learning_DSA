# Merge Sort Implementation in Python
# -----------------------------------
# Merge Sort is a classic divide-and-conquer sorting algorithm.
# It divides the list into halves, recursively sorts each half,
# and then merges the sorted halves to produce the sorted list.
#
# Time Complexity:
#   - Worst-case: O(n log n)
#   - Best-case: O(n log n)
#   - Average-case: O(n log n)
# Space Complexity: O(n) (requires additional space for merging)
#
# Reasoning:
#   - Merge Sort works by breaking the problem into smaller subproblems (divide),
#     solving each subproblem recursively (conquer), and then combining the results (merge).
#   - It is stable (does not change the relative order of equal elements).
#   - It is not in-place (requires extra space for merging).
#   - It is very efficient for large datasets and is the basis for many library sort functions.
#
# Example Usage Cases:
#   - Sorting large datasets where stability is important
#   - External sorting (sorting data that does not fit in memory)
#   - Used as part of hybrid sorting algorithms (e.g., TimSort in Python)
#   - Sorting linked lists (since merge sort does not require random access)


def merge_sort(arr):
    """
    Sorts a list in ascending order using the merge sort algorithm.
    Args:
        arr: List of comparable elements (e.g., integers, floats, strings).
    Returns:
        A new sorted list (original list is not modified).
    """
    # Base case: a list of zero or one elements is already sorted
    if len(arr) <= 1:
        return arr

    # Divide: find the middle index and split the list into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    # Merge: combine the sorted halves into a single sorted list
    merged = []
    i = j = 0  # Pointers for left_half and right_half

    # Compare elements from both halves and append the smaller one
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    # If there are remaining elements in either half, append them
    merged.extend(left_half[i:])
    merged.extend(right_half[j:])

    return merged


# Example usage:
if __name__ == "__main__":
    SORTED_LIST_LABEL = "Sorted list:  "
    # Example 1: Sorting integers
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", numbers)
    sorted_numbers = merge_sort(numbers)
    print(SORTED_LIST_LABEL, sorted_numbers)

    # Example 2: Sorting floats
    floats = [3.2, 1.5, 4.8, 2.9]
    print("\nOriginal list:", floats)
    sorted_floats = merge_sort(floats)
    print(SORTED_LIST_LABEL, sorted_floats)

    # Example 3: Sorting strings (alphabetically)
    words = ["banana", "apple", "cherry", "date"]
    print("\nOriginal list:", words)
    sorted_words = merge_sort(words)
    print(SORTED_LIST_LABEL, sorted_words)
