import math

def simple_areas(*args):

    area = {1: (lambda x: (1/4)*math.pi*x**2),
            2: (lambda x, y: x*y),
            3: (lambda x, y, z: math.sqrt(((x+y+z)/2)*(((x+y+z)/2)-x)*(((x+y+z)/2)-y)*(((x+y+z)/2)-z))) # Heron's formula
            }[len(args)](*args)

    return round(area, 2)
