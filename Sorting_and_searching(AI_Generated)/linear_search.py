# Linear Search Implementation in Python
# --------------------------------------
# Linear Search (also called Sequential Search) is the simplest searching algorithm.
# It checks each element of a list one by one until the desired element is found
# or the list ends.
#
# Time Complexity:
#   - Worst-case: O(n) (must check every element)
#   - Best-case: O(1) (target is the first element)
#   - Average-case: O(n)
# Space Complexity: O(1) (no extra space required)
#
# Reasoning:
#   - Linear search does not require the list to be sorted.
#   - It is easy to implement and works on any iterable (lists, arrays, etc.).
#   - It is inefficient for large datasets, but fine for small or unsorted data.
#
# Example Usage Cases:
#   - Searching for a value in a small or unsorted list
#   - Checking for the presence of an item in a collection
#   - When data is not sorted and performance is not critical

def linear_search(arr, target):
    """
    Searches for the target value in the list using linear search.
    Args:
        arr: List of elements to search through.
        target: The value to search for.
    Returns:
        The index of the target if found, else -1.
    """
    # Go through each element in the list
    for index, value in enumerate(arr):
        # If the current element matches the target, return its index
        if value == target:
            return index
    # If the loop completes, the target was not found
    return -1

# Example usage:
if __name__ == "__main__":
    # Example 1: Searching for an integer
    numbers = [5, 3, 8, 4, 2]
    target = 8
    print("List:", numbers)
    print(f"Searching for {target}...")
    result = linear_search(numbers, target)
    if result != -1:
        print(f"Found {target} at index {result}.")
    else:
        print(f"{target} not found in the list.")

    # Example 2: Searching for a string
    words = ["apple", "banana", "cherry", "date"]
    target_word = "cherry"
    print("\nList:", words)
    print(f"Searching for '{target_word}'...")
    result = linear_search(words, target_word)
    if result != -1:
        print(f"Found '{target_word}' at index {result}.")
    else:
        print(f"'{target_word}' not found in the list.")