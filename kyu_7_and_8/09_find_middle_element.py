# Find the middle element:
# As a part of this Kata, you need to create a function that when provided with a triplet,
# returns the index of the numerical element that lies between the other two elements.
# The input to the function will be an array of three distinct numbers (Haskell: a tuple).

## EXAMPLE
# gimme([2, 3, 1]) => 0
# gimme([5, 10, 14]) => 1


def gimme(input_array):
    x = input_array.copy()
    x.sort()
    num = x[1]
    return(input_array.index(num))
