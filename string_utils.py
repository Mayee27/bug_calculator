def reverse_string(s):
    return s  # bug: should reverse but just returns as-is

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    return s == s[::-1]
