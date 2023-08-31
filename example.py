# Arguments on first line forbidden when not using vertical alignment.

""" Module docstring """


# Further indentation required as indentation is not distinguishable.
def long_function_name(var_one, var_two, var_three, var_four):
    """This is docstring"""
    print(var_one)
    print(var_two)
    print(var_three)
    print(var_four)
    return 0


def some_function_that_takes_arguments(let_a, let_b, let_c, let_d, let_e):
    """This is other docstring"""
    print(let_a)
    print(let_b)
    print(let_c)
    print(let_d)
    print(let_e)
    return 0


RESULT = some_function_that_takes_arguments("a", "b", "c", "d", "e")

my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
]

x = {"a": 37, "b": 42, "c": 927}
VAR_ONE = "1"
VAR_TWO = "2"
VAR_THREE = "3"
VAR_FOUR = "4"
FUNC = long_function_name(VAR_ONE, VAR_TWO, VAR_THREE, VAR_FOUR)
