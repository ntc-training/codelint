# Further indentation required as indentation is not distinguishable.
def long_function_name(var_one, var_two, var_three, var_four):
    print(var_one)
    print(var_two)
    print(var_three)
    print(var_four)
    return "something"


def some_function_that_takes_arguments(one, two, three, four, five, six):
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
    print(six)
    return "something again"


# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name("1", "2", "3", "4")

result = some_function_that_takes_arguments(
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
)

my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
]

x = {"a": 37, "b": 42, "c": 927}
