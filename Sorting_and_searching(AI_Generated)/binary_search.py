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
