# Binary Search Implementation in Python
# --------------------------------------
# Binary Search is an efficient algorithm for finding an item from a sorted list.
# It works by repeatedly dividing the search interval in half.
# If the value of the search key is less than the item in the middle of the interval,
# narrow the interval to the lower half. Otherwise, narrow it to the upper half.
# Repeatedly check until the value is found or the interval is empty.
#
# Time Complexity:
#   - Worst-case: O(log n) (each step halves the search space)
#   - Best-case: O(1) (target is at the middle on the first check)
#   - Average-case: O(log n)
# Space Complexity: O(1) for iterative version, O(log n) for recursive version (due to call stack)
#
# Reasoning:
#   - Binary search is much faster than linear search for large, sorted datasets.
#   - It only works on sorted lists or arrays.
#   - It is widely used in computer science for searching and lookup operations.
#
# Example Usage Cases:
#   - Searching for a value in a sorted list or array
#   - Looking up entries in a sorted database or index
#   - Used in libraries and frameworks for fast searching


def binary_search(arr, target):
    """
    Searches for the target value in a sorted list using binary search.
    Args:
        arr: Sorted list of elements to search through.
        target: The value to search for.
    Returns:
        The index of the target if found, else -1.
    """
    left = 0  # Start of the search interval
    right = len(arr) - 1  # End of the search interval

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid
        # If the target is less than the middle element, search the left half
        elif arr[mid] > target:
            right = mid - 1
        # If the target is greater, search the right half
        else:
            left = mid + 1
    # If the loop completes, the target was not found
    return -1


# Example usage:
if __name__ == "__main__":
    # Example 1: Searching for an integer in a sorted list
    numbers = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    print("Sorted list:", numbers)
    print(f"Searching for {target}...")
    result = binary_search(numbers, target)
    if result != -1:
        print(f"Found {target} at index {result}.")
    else:
        print(f"{target} not found in the list.")

    # Example 2: Searching for a string in a sorted list
    words = ["apple", "banana", "cherry", "date", "fig"]
    target_word = "date"
    print("\nSorted list:", words)
    print(f"Searching for '{target_word}'...")
    result = binary_search(words, target_word)
    if result != -1:
        print(f"Found '{target_word}' at index {result}.")
    else:
        print(f"'{target_word}' not found in the list.")
