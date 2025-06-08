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
