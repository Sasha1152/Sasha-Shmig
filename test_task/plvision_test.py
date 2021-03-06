# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


def is_good_string(string):
    """
        >>> is_good_string('()')
        True
        >>> is_good_string('()[]{}')
        True
        >>> is_good_string('(]')
        False
        >>> is_good_string('([)]')
        False
        >>> is_good_string('{[]}')
        True
        >>> is_good_string('   ')
        True
    """

    brackets = '([{}])'
    opening_brackets = '([{'
    brackets_dict = {'(': ')', '[': ']', '{': '}'}
    opened_bracket = []

    for i in string:
        if i in brackets:
            if i in opening_brackets:
                opened_bracket.append(i)

            elif i == brackets_dict.get(opened_bracket[-1]):
                opened_bracket.pop()

    return not len(opened_bracket)


if __name__ == '__main__.py':
    import doctest
    doctest.testmod()
