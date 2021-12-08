def valid_parentheses(string):
    """A function that takes a string of parentheses,
    and determines if the order of the parentheses is valid."""
    count = 0
    brackets = [x for x in string if x == '(' or x == ')']
    for i in brackets:
        if count >= 0:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
        else:
            return False
    if count == 0:
        return True
    else:
        return False
        
    

def test_valid_parentheses():
    assert valid_parentheses("()")
    assert valid_parentheses("(())((()())())")
    assert valid_parentheses("()")

test_valid_parentheses()

