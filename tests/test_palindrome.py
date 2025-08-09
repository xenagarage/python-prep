from examples/palindrome import is_palindrome
def test_is_palindrome():
    assert is_palindrome("aba") is True
    assert is_palindrome("abc") is False