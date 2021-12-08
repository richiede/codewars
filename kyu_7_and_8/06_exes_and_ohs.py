def xo(s):
    """Check to see if a string has the same amount of 'x's and 'o's.
    The method must return a boolean and be case insensitive.
    The string can contain any char."""
    x = [x.lower() for x in s if x == 'x' or x == 'X']
    o = [o.lower() for o in s if o == 'o' or o == 'O']
    if len(x) == len(o):
        return True
    else:
        return False

def test_xo():
    """Test the xo function"""
    assert xo('ooxx')
    assert xo('XxOoMLKsd')
    assert xo('XXOO')
    assert xo('xO')
    assert xo('xoooxx')

test_xo()
