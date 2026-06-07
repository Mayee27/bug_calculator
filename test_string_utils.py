import pytest
from string_utils import reverse_string, count_vowels, is_palindrome

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou") == 5

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
