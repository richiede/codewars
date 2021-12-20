def solution(s):
    """
    the function will break up camel casing, using a space between words
    Example:
    "camelCasing"  =>  "camel Casing"
    "identifier"   =>  "identifier"
    ""             =>  ""
    """
    my_var = ''
    my_list = []
    for i in s:
        if i.islower():
            my_var += i
        else:
            my_list.append(my_var)
            my_var = i
    my_list.append(my_var)
    return(' '.join(my_list))
