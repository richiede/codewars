# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    counter = 0
    space_list = []
    for i in range(len(text)):
	    if text[i] == " ":
	        counter += 1
	    else:
	        space_list.append(counter)
	        counter = 0
            
    final_space = [x for x in space_list if x != 0]
    
    my_list = text.split()

    for i in range(len(final_space)):
        my_list.insert(i*2+1, ' ' * final_space[i])
    
    rev_list = [x[::-1] for x in my_list]
    return(''.join(rev_list))
