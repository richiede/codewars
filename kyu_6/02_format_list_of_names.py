def namelist(names):
    """Given: an array containing hashes of names
    Return: a string formatted as a list of names
    separated by commas except for the last two names,
    which should be separated by an ampersand.

Example:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# returns 'Bart'

# namelist([])
# returns ''
    """
    my_string = ''
    name_list = [i['name'] for i in names]
    count = range(len(name_list)-1)
    splitters = [', ' for i in count]
    if len(splitters) > 0:
        splitters[-1] = ' & '
    for i in range(len(name_list)):
        try:
            my_string += name_list[i]
            my_string += splitters[i]          
        except IndexError:
            continue
    return(my_string)
