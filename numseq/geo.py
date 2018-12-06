"""This package returns a number depending on a cube, square, or a triangle"""



def square(num):
    """returns a squared number"""
    sq_num = num ** 2
    return sq_num

def triangle(num):
    """returns the area of a triangle"""
    sq_num = square(num)
    tri = sq_num / 2
    return tri

def cube(num):
    """returns the a cubed number"""
    cubed = num ** 3
    return cubed


    

