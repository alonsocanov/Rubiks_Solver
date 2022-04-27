import sys
import numpy as np


class Cubie(object):
    def __init__(self, index=None, orientation=None, colors=None) -> None:
        self.index = index
        self.orientation = orientation
        self.colors = colors

    def __str__(self) -> str:
        return str(self.index) + ', ' + str(self.orientation)


class Color(object):
    def __init__(self, index=None, color=None) -> None:
        self.index = index
        self.color = color

    def __str__(self) -> str:
        return str(self.index) + ', ' + str(self.color)


class Rubik(object):

    face = ('UP', 'LEFT', 'FRONT', 'RIGHT', 'BACK', 'DOWN')
    color = ('WHITE', 'GREEN', 'RED', 'BLUE', 'ORANGE', 'YELLOW')
    edges = ('UB', 'UR', 'UF', 'UL', 'FR', 'FL',
             'BL', 'BR', 'DF', 'DL', 'DB', 'DR')
    corners = ('ULB', 'URB', 'URF', 'ULF', 'DLF', 'DLB', 'DRB', 'DRF')
    move = ('L', 'L_', 'L2', 'R', 'R_', 'R2', 'U', 'U_', 'U2', 'D', 'D_', 'D2', 'F', 'F_', 'F2', 'B', 'B_',
            'B2', 'Y', 'Y_', 'Y2', 'X', 'X_', 'X2', 'Z', 'Z_', 'Z2', 'M', 'M_', 'M2', 'E', 'E_', 'E2', 'S', 'S_', 'S2')

    color_corners = {'ULB': ('RED', 'BLUE', 'YELLOW'),
                     'URB': ('RED', 'GREEN', 'YELLOW'),
                     'URF': ('RED', 'GREEN', 'WHITE'),
                     'ULF': ('RED', 'BLUE', 'WHITE'),
                     'DLF': ('ORANGE', 'BLUE', 'WHITE'),
                     'DLB': ('ORANGE', 'BLUE', 'YELLOW'),
                     'DRB': ('ORANGE', 'GREEN', 'YELLOW'),
                     'DRF': ('ORANGE', 'GREEN', 'WHITE')}

    color_edges = {'UB': ('RED', 'YELLOW'),
                   'UR': ('RED', 'GREEN'),
                   'UF': ('RED', 'WHITE'),
                   'UL': ('RED', 'BLUE'),
                   'FR': ('WHITE', 'GREEN'),
                   'FL': ('WHITE', 'BLUE'),
                   'BL': ('YELLOW', 'BLUE'),
                   'BR': ('YELLOW', 'GREEN'),
                   'DF': ('ORANGE', 'WHITE'),
                   'DL': ('ORANGE', 'BLUE'),
                   'DB': ('ORANGE', 'YELLOW'),
                   'DR': ('ORANGE', 'GREEN')}

    edge = []
    corner = []
    center = []

    def __init__(self, cube=None):
        pass

    def create_solved_cube(self):
        # Edges
        for i in range(12):
            temp = Cubie(index=i, orientation=0)
            self.edge += [temp]
        # Corners
        for i in range(8):
            temp = Cubie(intex=i, orientation=0)
            self.corner += [temp]
        # Centers
        color_dict = {0: 'RED', 1: 'BLUE',  2: 'WHITE',
                      3: 'GREEN', 4: 'YELLOW', 5: 'ORANGE'}
        for key in list(color_dict.keys()):
            color = Color(index=key, color=color_dict[key])
            self.centers += [color]

    def get_edge_colors(self, edge: Cubie):

        return self.color_edges[edge.index]
