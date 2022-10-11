"""Test module doc string"""
# Arguments on first line forbidden when not using vertical alignment.
# Further indentation required as indentation is not distinguishable.


def long_function_name(var_one, var_two, var_three, var_four):
    """To find long function name.
    Args:
        var_one (int): The integer value.
        var_two (int): The integer value.
        var_three (int): The integer value.
        var_four (int): The integer value.
    """
    print(var_one, var_two, var_three, var_four)


long_function_name(var_one=1, var_two=2, var_three=3, var_four=4)


def some_function_that_takes_arguments(*args):
    """To fix undefined variable
    Args:
        args: The variable arguments.

    Returns:
        list: The list of variables
    """
    return args


RESULT = some_function_that_takes_arguments("a", "b", "c", "d", "e", "f")

my_list = [1, 2, 3, 4, 5, 6]

x = {"a": 37, "b": 42, "c": 927}
