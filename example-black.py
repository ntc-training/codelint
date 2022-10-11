# Arguments on first line forbidden when not using vertical alignment.
my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
]

var_one, var_two, var_three, var_four, var_five, var_six = my_list


# Further indentation required as indentation is not distinguishable.
def long_function_name(val1, val2, val3, val4):
    """
    Long Function name
    :param val1:
    :param val2:
    :param val3:
    :param val4:
    :return: variable.
    """
    print(val1)


long_function_name(var_one, var_two, var_three, var_four)


def some_function_that_takes_arguments(*args):
    return args


result = some_function_that_takes_arguments("a", "b", "c", "d", "e", "f")

x = {"a": 37, "b": 42, "c": 927}
