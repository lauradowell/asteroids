import math
import numpy as np

# Rotate a 2D vector by a certain angle
def rotate(vector, angle):
	# Action required!
    
    # def vector
    #def mouse pos1
    #def mousepos2

    # a = distance  between vector and mouse1pos
    # b  = distance between vector mouse2pos
    # c = distance between mousepos1 and mousepos2

    #calculate angle using the distances of a, b , c
    #from math import acos, degrees
    #>>> degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
    return vector

# Map a value from one range to another
def map(n, start1, stop1, start2, stop2):
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2;

    if newval > stop2:
        return stop2
    elif newval < start2:
        return start2
    else:
        return newval