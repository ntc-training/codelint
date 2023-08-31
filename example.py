"""This is a test script we are to perform tests on"""


def long_function_name(*args):
    """Further indentation required as indentation is not distinguishable."""
    return args


# Arguments on first line forbidden when not using vertical alignment.
NEAT = long_function_name(1, 2, 3, 4, 5, 6, 7)


def some_function_that_takes_arguments(*args):
    """# This is a function that makes requirements"""
    return args


result = some_function_that_takes_arguments("a", "b", "c", "d", "e", "f")


my_list = [1, 2, 3, 4, 5, 6]


x = {"a": 37, "b": 42, "c": 927}
