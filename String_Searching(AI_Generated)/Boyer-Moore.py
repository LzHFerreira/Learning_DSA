# Boyer-Moore String Search Implementation in Python
# --------------------------------------------------
# The Boyer-Moore algorithm is an efficient string searching algorithm.
# It uses information gathered during the preprocessing of the pattern to skip sections of the text,
# making it much faster than naive search for most practical cases.
#
# Time Complexity:
#   - Worst-case: O(n * m) (rare, with certain patterns and texts)
#   - Best/average-case: O(n) (often sublinear in practice)
#     where n = length of text, m = length of pattern
# Space Complexity: O(m + k), where k is the size of the alphabet (for the bad character table)
#
# Reasoning:
#   - Boyer-Moore preprocesses the pattern to create "bad character" and "good suffix" tables.
#   - When a mismatch occurs, it uses these tables to skip ahead in the text, rather than checking every position.
#   - This makes it very efficient for large texts and patterns.
#   - It is the basis for many real-world search tools and libraries.
#
# Example Usage Cases:
#   - Searching for a substring in large texts (editors, search engines)
#   - DNA/protein sequence analysis
#   - Plagiarism detection
#   - Any application where fast string matching is required


def build_bad_character_table(pattern):
    """
    Builds the bad character table for Boyer-Moore.
    Args:
        pattern: The pattern string.
    Returns:
        A dictionary mapping each character to its last occurrence in the pattern.
    """
    table = {}
    for i, char in enumerate(pattern):
        table[char] = i  # Store the last index of each character in the pattern
    return table


def boyer_moore_search(text, pattern):
    """
    Searches for all occurrences of the pattern in the text using Boyer-Moore algorithm (bad character rule only).
    Args:
        text: The string to search within.
        pattern: The substring pattern to search for.
    Returns:
        A list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    bad_char_table = build_bad_character_table(pattern)  # Preprocess the pattern
    result = []  # List to store the starting indices of matches
    s = 0  # s is the shift of the pattern with respect to text

    while s <= n - m:
        j = m - 1  # Start comparing from the end of the pattern

        # Move backwards through the pattern as long as characters match
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            # Pattern found at shift s
            result.append(s)
            # Shift pattern so that the next character in text aligns with the last occurrence in pattern
            s += m - bad_char_table.get(text[s + m], -1) if s + m < n else 1
        else:
            # Shift pattern so that the bad character in text aligns with its last occurrence in pattern
            bad_char_shift = j - bad_char_table.get(text[s + j], -1)
            s += max(1, bad_char_shift)

    return result


# Example usage:
if __name__ == "__main__":
    PATTERN_FOUND_MSG = "Pattern found at indices:"

    # Example 1: Simple substring search
    text = "abacaabadcabacabaabb"
    pattern = "abacab"
    print(f"Text: '{text}'")
    print(f"Pattern: '{pattern}'")
    matches = boyer_moore_search(text, pattern)
    print(PATTERN_FOUND_MSG, matches)

    # Example 2: Pattern not present
    text2 = "hello world"
    pattern2 = "test"
    print(f"\nText: '{text2}'")
    print(f"Pattern: '{pattern2}'")
    matches2 = boyer_moore_search(text2, pattern2)
    print(PATTERN_FOUND_MSG, matches2)

    # Example 3: Multiple matches
    text3 = "ABC ABCDAB ABCDABCDABDE"
    pattern3 = "ABCDABD"
    print(f"\nText: '{text3}'")
    print(f"Pattern: '{pattern3}'")
    matches3 = boyer_moore_search(text3, pattern3)
    print(PATTERN_FOUND_MSG, matches3)
