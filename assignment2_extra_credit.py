from mesh import Mesh
from pprint import pprint

from screen import Screen
import numpy as np

if __name__ == '__main__':
    mesh = Mesh.from_stl("unit_cube.stl")

    #set up the screen
    WIDTH  = 500
    HEIGHT = 500

    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 0)

    screen = Screen(WIDTH, HEIGHT)

    image_buffer = np.full((HEIGHT, WIDTH, 3), COLOR2)

    #define simple transformations 
    s  = 100
    dx = 200
    dy = 200

    #TODO: loop over each face, apply transformations to x and y components
    #      and draw lines between each vertex of each face
