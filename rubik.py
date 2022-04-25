import numpy as np


class Rubik(object):
    face = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'R': 4, 'L': 5}
    idx_face = dict([(v, k) for k, v in face.items()])
    color = {'w': 0, 'y': 1, 'b': 2, 'g': 3, 'o': 4, 'r': 5}
    normals = [np.array([0., 1., 0.]), np.array([0., -1., 0.]),
               np.array([0., 0., 1.]), np.array([0., 0., -1.]),
               np.array([1., 0., 0.]), np.array([-1., 0., 0.])]
    xdirs = [np.array([1., 0., 0.]), np.array([1., 0., 0.]),
             np.array([1., 0., 0.]), np.array([-1., 0., 0.]),
             np.array([0., 0., -1.]), np.array([0., 0., 1.])]


def __init__(self, N):
    pass
