import math

def longest_side(a,b):
    """
    Function to fine the length of the longest side of a right triangle.

    :arg a: side a of the triangle
    :arg b: side b of the triangle

    :return: length of the longest side c as float
    """
    return math.sqrt(a*a + b*b)
if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(3,4))

