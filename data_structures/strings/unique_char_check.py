"""
Unique Character Check

This module provides a function to check if all characters in a string are unique.

Problem:
Given a string, determine if it has all unique characters (no repeated characters).

Examples:
- "abcd" -> True (all characters are unique)
- "aabc" -> False (character 'a' is repeated)

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(min(n, k)) where k is the size of the character set
"""
from collections import Counter
from typing import Dict, Set


def unique_char_check(string: str) -> bool:
    """
    Check if all characters in a string are unique.

    This function uses Counter from the collections module to count
    the occurrences of each character in the string. If the number of
    unique characters equals the length of the string, then all characters
    are unique.

    Args:
        string: The input string to check

    Returns:
        True if all characters in the string are unique, False otherwise

    Examples:
        >>> unique_char_check("abcd")
        True
        >>> unique_char_check("aabc")
        False
    """
    # Count occurrences of each character
    character_count: Dict[str, int] = Counter(string)

    # If the number of unique characters equals the length of the string,
    # then all characters are unique
    return len(character_count) == len(string)


def unique_char_check_set(string: str) -> bool:
    """
    Alternative implementation using a set.

    This function uses a set to track seen characters. If a character
    is encountered that's already in the set, the function returns False.

    Args:
        string: The input string to check

    Returns:
        True if all characters in the string are unique, False otherwise

    Examples:
        >>> unique_char_check_set("abcd")
        True
        >>> unique_char_check_set("aabc")
        False
    """
    seen: Set[str] = set()

    for char in string:
        if char in seen:
            return False
        seen.add(char)

    return True


if __name__ == "__main__":
    # Test with user input
    user_input = input("Enter a string to check for unique characters: ")
    result = unique_char_check(user_input)

    print(f"Using Counter: '{user_input}' has all unique characters: {result}")

    # Also test the alternative implementation
    result_set = unique_char_check_set(user_input)
    print(f"Using Set: '{user_input}' has all unique characters: {result_set}")

    # Additional test cases
    test_cases = ["abcd", "aabc", "", "a", "abcdefghijklmnopqrstuvwxyz"]

    print("\nAdditional test cases:")
    for test in test_cases:
        result = unique_char_check(test)
        print(f"'{test}': {result}")
