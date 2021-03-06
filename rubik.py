import sys
from turtle import color
import numpy as np


class Cubie(object):
    def __init__(self, index=None, orientation=None, colors=None, position=None) -> None:
        self.index = index
        self.orientation = orientation
        self.color = colors
        self.position = position

    def set_orientation(self, orientation: int):
        if len(self.color) == 3:
            if orientation > 2 or orientation < 0:
                message = 'Orientation not valid'
                sys.exit(message)
            self.orientation = orientation

        elif len(self.color) == 2:
            if orientation > 1 or orientation < 0:
                message = 'Orientation not valid'
                sys.exit(message)
            self.orientation = orientation
        else:
            message = 'Orientation not valid'
            sys.exit(message)

    def __str__(self) -> str:
        return str(self.index) + ', ' + str(self.orientation)


class Color(object):
    def __init__(self, index=None, color=None) -> None:
        self.index = index
        self.color = color

    def __str__(self) -> str:
        return str(self.index) + ', ' + str(self.color)


class Rubik(object):

    faces = ('UP', 'LEFT', 'FRONT', 'RIGHT', 'BACK', 'DOWN')
    colors = ('WHITE', 'GREEN', 'RED', 'BLUE', 'ORANGE', 'YELLOW')
    abr_colors = {'WHITE': 'WHI', 'GREEN': 'GRE', 'RED': 'RED',
                  'BLUE': 'BLU', 'ORANGE': 'ORA', 'YELLOW': 'YEL'}
    edges = ('UB', 'UR', 'UF', 'UL', 'FR', 'FL',
             'BL', 'BR', 'DF', 'DL', 'DB', 'DR')
    corners = ('ULB', 'URB', 'URF', 'ULF', 'DLF', 'DLB', 'DRB', 'DRF')
    move = ('L', 'L_', 'L2', 'R', 'R_', 'R2', 'U', 'U_', 'U2', 'D', 'D_', 'D2', 'F', 'F_', 'F2', 'B', 'B_',
            'B2', 'Y', 'Y_', 'Y2', 'X', 'X_', 'X2', 'Z', 'Z_', 'Z2', 'M', 'M_', 'M2', 'E', 'E_', 'E2', 'S', 'S_', 'S2')

    color_index = {('UP', 0, 0): ('ULB', 0), ('UP', 0, 1): ('UB', 0),
                   ('UP', 0, 2): ('URB', 0), ('UP', 1, 0): ('UL', 0),
                   ('UP', 1, 2): ('UR', 0), ('UP', 2, 0): ('ULF', 0),
                   ('UP', 2, 1): ('UF', 0), ('UP', 2, 2): ('URF', 0),
                   ('FRONT', 0, 0): ('ULF', 2), ('FRONT', 0, 1): ('UF', 1),
                   ('FRONT', 0, 2): ('URF', 2), ('FRONT', 1, 0): ('FL', 0),
                   ('FRONT', 1, 2): ('FR', 0), ('FRONT', 2, 0): ('DLF', 2),
                   ('FRONT', 2, 1): ('DF', 1), ('FRONT', 2, 2): ('DRF', 2),
                   ('RIGHT', 0, 0): ('URF', 1), ('RIGHT', 0, 1): ('UR', 1),
                   ('RIGHT', 0, 2): ('URB', 1), ('RIGHT', 1, 0): ('FR', 1),
                   ('RIGHT', 1, 2): ('BR', 1), ('RIGHT', 2, 0): ('DRF', 1),
                   ('RIGHT', 2, 1): ('DR', 1), ('RIGHT', 2, 2): ('DRB', 1),
                   ('LEFT', 0, 0): ('ULB', 1), ('LEFT', 0, 1): ('UL', 1),
                   ('LEFT', 0, 2): ('ULF', 1), ('LEFT', 1, 0): ('BL', 1),
                   ('LEFT', 1, 2): ('FL', 1), ('LEFT', 2, 0): ('DLB', 1),
                   ('LEFT', 2, 1): ('DL', 1), ('LEFT', 2, 2): ('DLF', 1),
                   ('BACK', 0, 0): ('URB', 2), ('BACK', 0, 1): ('UB', 1),
                   ('BACK', 0, 2): ('ULB', 2), ('BACK', 1, 0): ('BR', 0),
                   ('BACK', 1, 2): ('BL', 0), ('BACK', 2, 0): ('DRB', 2),
                   ('BACK', 2, 1): ('DB', 1), ('BACK', 2, 2): ('DLB', 2),
                   ('DOWN', 0, 0): ('DLB', 0), ('DOWN', 0, 1): ('DB', 0),
                   ('DOWN', 0, 2): ('DRB', 0), ('DOWN', 1, 0): ('DL', 0),
                   ('DOWN', 1, 2): ('DR', 0), ('DOWN', 2, 0): ('DLF', 0),
                   ('DOWN', 2, 1): ('DF', 0), ('DOWN', 2, 2): ('DRF', 0)}

    color_corners = {}
    color_edges = {}

    edge = {}
    corner = {}
    center = {}

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
            self.edge[val] = temp
        # Corners
        for i, val in enumerate(self.corners):
            colors = self.color_corners[val]
            temp = Cubie(index=i, orientation=0, colors=colors, position=val)
            self.corner[val] = temp
        # Centers
        for idx, color in enumerate(colors):
            face = Color(index=idx, color=color)
            self.center[color] = face

    def get_edge_colors(self, pos: str):
        edge = self.edge[pos]
        colors = edge.color
        if edge.orientation == 1:
            colors = colors[1], colors[0]
        return colors

    def get_corner_colors(self, pos: str):
        corner = self.corner[pos]
        colors = corner.color
        if corner.orientation == 1:
            colors = colors[2], colors[1], colors[0]
        elif corner.orientation == 2:
            colors = colors[2], colors[0], colors[1]
        return colors

    def get_color(self, face: str, row: int, column: int):
        edge, color_idx = self.color_index[(face, row, column)]
        if len(edge) == 3:
            return self.get_corner_colors(edge)[color_idx]
        elif len(edge) == 2:
            return self.get_edge_colors(edge)[color_idx]

    def test_all_colors(self):
        for face in self.faces:
            for row in range(3):
                for col in range(3):
                    if row != 1 or col != 1:
                        color = self.get_color(face, row, col)

    def up(self):
        temp_edge = self.edge['UF']
        self.edge['UF'] = self.edge['UR']
        self.edge['UR'] = self.edge['UB']
        self.edge['UB'] = self.edge['UL']
        self.edge['UL'] = temp_edge

        temp_corner = self.corner['URF']
        self.corner['URF'] = self.corner['URB']
        self.corner['URB'] = self.corner['ULB']
        self.corner['ULB'] = self.corner['ULF']
        self.corner['ULF'] = temp_corner

    def down(self):
        temp_edge = self.edge['DF']
        self.edge['DF'] = self.edge['DL']
        self.edge['DL'] = self.edge['DB']
        self.edge['DB'] = self.edge['DR']
        self.edge['DR'] = temp_edge

        temp_corner = self.corner['DRF']
        self.corner['DRF'] = self.corner['DLF']
        self.corner['DLF'] = self.corner['DLB']
        self.corner['DLB'] = self.corner['DRB']
        self.corner['DRB'] = temp_corner

    def right(self):
        temp_edge = self.edge['UR']
        self.edge['UR'] = self.edge['FR']
        self.edge['FR'] = self.edge['DR']
        self.edge['DR'] = self.edge['BR']
        self.edge['BR'] = temp_edge

        temp_corner = self.corner['URF']
        self.corner['URF'] = self.corner['DRF']
        self.corner['DRF'] = self.corner['DRB']
        self.corner['DRB'] = self.corner['URB']
        self.corner['URB'] = temp_corner

    def __str__(self):
        string = ''

        face = 'UP'
        for row in range(3):
            string += '            '
            for col in range(3):
                if row != 1 or col != 1:
                    color = self.get_color(face, row, col)
                    string += self.abr_colors[color] + ' '
                else:
                    string += '    '
            string += '\n'

        face_order = ['LEFT', 'FRONT', 'RIGHT', 'BACK']
        idx_face = 0
        row = 0
        col = 0
        while idx_face < len(face_order) and col < 3 and row < 3:

            face = face_order[idx_face]
            if row != 1 or col != 1:
                color = self.get_color(face, row, col)
                string += self.abr_colors[color] + ' '
            else:
                string += '    '
            col += 1
            if col == 3 and idx_face < len(face_order):
                col = 0
                idx_face += 1
            if idx_face == len(face_order):
                row += 1
                idx_face = 0
                string += '\n'

        face = 'DOWN'
        for row in range(3):
            string += '            '
            for col in range(3):
                if row != 1 or col != 1:
                    color = self.get_color(face, row, col)
                    string += self.abr_colors[color] + ' '
                else:
                    string += '    '
            string += '\n'

        return string
