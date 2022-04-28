import sys
import numpy as np


class Cubie(object):
    def __init__(self, index=None, orientation=None, colors=None, position=None) -> None:
        self.index = index
        self.orientation = orientation
        self.color = colors
        self.position = position

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
    # position (face row column)
    positions = {'ULB': (0, 0, 0), 'UB': (0, 0, 1), 'ULR': (0, 0, 2), 'UL': (0, 1,  0),
                 'UR': (0, 1, 2), 'ULF': (0, 2, 0), 'UF': (0, 2, 1), 'URF': (0, 2, 2)}

    color_corners = {}
    color_edges = {}

    edge = []
    corner = []
    center = []

    def __init__(self, cube=None):
        pass

    def create_solved_cube(self):
        self.color_edges = {'UB': ('RED', 'YELLOW'),
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
        self.color_corners = {'ULB': ('RED', 'BLUE', 'YELLOW'),
                              'URB': ('RED', 'GREEN', 'YELLOW'),
                              'URF': ('RED', 'GREEN', 'WHITE'),
                              'ULF': ('RED', 'BLUE', 'WHITE'),
                              'DLF': ('ORANGE', 'BLUE', 'WHITE'),
                              'DLB': ('ORANGE', 'BLUE', 'YELLOW'),
                              'DRB': ('ORANGE', 'GREEN', 'YELLOW'),
                              'DRF': ('ORANGE', 'GREEN', 'WHITE')}
        # Edges
        for i, val in enumerate(self.edges):
            colors = self.color_edges[val]
            temp = Cubie(index=i, orientation=0, colors=colors, position=val)
            self.edge += [temp]
        # Corners
        for i, val in enumerate(self.corners):
            colors = self.color_corners[val]
            temp = Cubie(index=i, orientation=0, colors=colors, position=val)
            self.corner += [temp]
        # Centers
        color_dict = {0: 'RED', 1: 'BLUE',  2: 'WHITE',
                      3: 'GREEN', 4: 'YELLOW', 5: 'ORANGE'}
        for key in list(color_dict.keys()):
            color = Color(index=key, color=color_dict[key])
            self.center += [color]

    def get_edge_colors(self, pos: str):
        colors = self.color_edges[pos]
        edge = self.edge[ind]
        if edge.orientation == 1:
            colors[0], colors[1] = colors[1], colors[0]
        return colors

    def get_corner_colors(self, pos: str):
        colors = self.color_edges[pos]
        corner = self.corner[ind]
        if corner.orientation == 1:
            colors[0], colors[1], colors[2] = colors[2], colors[1], colors[0]
        elif corner.orientation == 2:
            colors[0], colors[1], colors[2] = colors[2], colors[0], colors[1]
        return colors

    def get_color(self, face: str, row: int, column: int):
        if face == 'UP':
            if row == 0:
                if column == 0:
                    return self.get_corner_colors()
