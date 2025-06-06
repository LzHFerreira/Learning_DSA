# Naive String Search (Brute Force) Implementation in Python
# ----------------------------------------------------------
# The naive string search algorithm (also called brute force search)
# checks for the presence of a pattern (substring) in a text by
# checking every possible position in the text where the pattern could fit.
#
# Time Complexity:
#   - Worst-case: O((n - m + 1) * m) ≈ O(n * m)
#     where n = length of text, m = length of pattern
#   - Best-case: O(n) (if pattern is found at the first position)
# Space Complexity: O(1) (no extra space required)
#
# Reasoning:
#   - The algorithm slides the pattern over the text one character at a time,
#     and for each position, checks if the substring matches the pattern.
#   - It is simple to implement but inefficient for large texts or patterns.
#   - It does not preprocess the pattern or text, unlike more advanced algorithms
#     (e.g., KMP, Boyer-Moore).
#
# Example Usage Cases:
#   - Educational purposes (to teach string searching concepts)
#   - Small texts or patterns where performance is not critical
#   - Situations where simplicity is more important than speed


def naive_search(text, pattern):
    """
    Searches for all occurrences of the pattern in the text using naive search.
    Args:
        text: The string to search within.
        pattern: The substring pattern to search for.
    Returns:
        A list of starting indices where the pattern is found in the text.
    """
    n = len(text)  # Length of the text
    m = len(pattern)  # Length of the pattern
    result = []  # List to store the starting indices of matches

    # Loop through every possible starting position in the text
    for i in range(n - m + 1):
        match = True  # Assume a match unless proven otherwise
        # Check if the substring matches the pattern
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False  # Mismatch found, break out of inner loop
                break
        if match:
            result.append(i)  # Pattern found at index i

    return result


# Example usage:
if __name__ == "__main__":
    PATTERN_FOUND_MSG = "Pattern found at indices:"

    # Example 1: Simple substring search
    text = "abracadabra"
    pattern = "abra"
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    matches = naive_search(text, pattern)
    print(PATTERN_FOUND_MSG, matches)

    # Example 2: Pattern not present
    text2 = "hello world"
    pattern2 = "test"
    print(f"\nText: '{text2}'")
    print(f"Pattern: '{pattern2}'")
    matches2 = naive_search(text2, pattern2)
    print(PATTERN_FOUND_MSG, matches2)

    # Example 3: Multiple overlapping matches
    text3 = "aaaaa"
    pattern3 = "aa"
    print(f"\nText: '{text3}'")
    print(f"Pattern: '{pattern3}'")
    matches3 = naive_search(text3, pattern3)
    print(PATTERN_FOUND_MSG, matches3)
