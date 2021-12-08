def printer_error(s):
    """returns errors rate if letters in a given string are not in the 
    alphabetical range of a - m
    example: s="aaabbbbhaijjjm" printer_error(s) => "0/14
    example: s="aaaxbbbbyyhwawiwjjjwwm" printer_error(s) => "8/22"""""
    correct_codes = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                     'h', 'i', 'j', 'k', 'l', 'm']
    counter = 0
    total = len(s)
    for i in s:
        if i not in correct_codes:
            counter += 1
    return(f"{counter}/{total}")
