def count(string):
    """
    Count all the occurring characters in a string, adding character and
    number of instances to a dictionary.
    example: "aba" should return {'a': 2, 'b': 1}
    
    """
    my_dict = {}
    for i in string:
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] = my_dict[i] + 1
    return my_dict
