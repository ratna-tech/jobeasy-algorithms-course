#Given an integral number, determine if it's a square number
import math
def find_if_squarenum(num):
    if num < 0:
        return False
    if num == 0:
        return True
    else:
        root = math.sqrt(num)
        return root.is_integer()

print(find_if_squarenum(144))