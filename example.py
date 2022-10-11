"""Module Docstrings"""
# Arguments on first line forbidden when not using vertical alignment.
var_one, var_two, var_three, var_four, var_five, var_six, var_seven = (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
)


# Further indentation required as indentation is not distinguishable.
def long_function_name(val1, val2, val3, val4):
    """
    Long Function Name.
    :param val1: value 1
    :param val2: value 2
    :param val3: value 3
    :param val4: value 4
    :return: None
    """
    print(val1, val2, val3, val4)


long_function_name(var_one, var_two, var_three, var_four)


def some_function_that_takes_arguments(*kwargs):
    """
    Cover up functions for some function that takes arguments.
    :param kwargs: multiple kwargs
    :return: kwargs
    """
    return kwargs


result = some_function_that_takes_arguments("a", "b", "c", "d", "e", "f")
my_list = [1, 2, 3, 4, 5, 6]
x = {"a": 37, "b": 42, "c": 927}
