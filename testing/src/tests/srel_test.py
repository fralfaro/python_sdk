import utils.srel
import pytest

@pytest.mark.parametrize(
    "word, expected", 
    [
        ('kayak', True), 
        ('civic', True), 
        ('forest', False)
    ]
)
def test_palindrome(word, expected):

    val = utils.srel.is_palindrome(word)
    assert val == expected
