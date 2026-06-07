
def reverse_string(s):
    # Fix: changed to return the reversed string using slicing with a step of -1
    return s[::-1]  # was: return s

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    return s == s[::-1]
