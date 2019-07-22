import math


def is_palindrome_number(x):

    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1

    if num_digits == 1:
        return True

    half_digits = 0
    for step in range(num_digits // 2):
        last_digit = x % 10
        half_digits *= 10
        half_digits += last_digit
        x //= 10

    if num_digits % 2 == 1:
        x //= 10

    return x == half_digits


if __name__ == '__main__':

    assert is_palindrome_number(0)
    assert is_palindrome_number(1)
    assert is_palindrome_number(7)
    assert is_palindrome_number(11)
    assert is_palindrome_number(121)
    assert is_palindrome_number(333)
    assert is_palindrome_number(12321)

    assert not is_palindrome_number(-1)
    assert not is_palindrome_number(12)
    assert not is_palindrome_number(100)
    assert not is_palindrome_number(123456)
