#! /usr/bin/env python

var_one = "blah"
var_two = "bleh"
var_three = "blih"
var_four = "bloh"
var_five = "bluh"
var_six = "blyh"
var_seven = "blaeiouyh"

# Further indentation required as indentation is not distinguishable.
def long_function_name(var_one, var_two, var_three, var_four):
    print(var_one)


# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(
    var_one, var_two, var_three, var_four, var_five, var_six, var_seven
)

def some_function_that_takes_arguments(var_one, var_two, var_three, var_four, var_five, var_six):
    print(var_one)


result = some_function_that_takes_arguments("a", "b", "c", "d", "e", "f")

my_list = [
    1,
    2,
    3,
    4,
    5,
    6
]

x = {"a": 37, "b": 42, "c": 927}
