# square every digit of a number and concatenate them.
# For example, if we run 9119 through the function,
# 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer


def square_digits(num):
    a = str(num)
    b = [int(x)**2 for x in a]
    c = [str(x) for x in b]
    d = ''.join(c)
    e = int(d)
    return(e)

digit = square_digits(9119)
print(digit)
