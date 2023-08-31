# Arguments on first line forbidden when not using vertical alignment.


var_one = "1"
var_two = "2"
var_three = "3"
var_four = "4"
var_five = "5"
var_six = "5"
var_seven = "5"


# Further indentation required as indentation is not distinguishable.
def long_function_name(var_one, var_two, var_three, var_four):
    print(var_one)


foo = long_function_name(
    var_one, var_two, var_three, var_four, var_five, var_six, var_seven
)


def some_function_that_takes_arguments(
    var_one, var_two, var_three, var_four, var_five, var_six
):
    pass


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
