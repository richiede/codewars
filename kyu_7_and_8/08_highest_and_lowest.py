def high_and_low(numbers):
    """given a string of space separated numbers,
    return the highest and lowest number as space separated string.
    high_and_low("1 2 -3 4 5") # return "5 -3"
    """
    my_list = [int(x) for x in numbers.split()]
    my_list.sort()
    return(str(my_list[-1]) + ' ' + str(my_list[0]))
