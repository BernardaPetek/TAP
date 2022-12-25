import itertools
import unittest
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from linesweeptriangulation import triangulate


def najdisoseda(trikotnik1, T1):
    st = 0
    sosedi = []
    for triangle in T1:
        edge = []
        if trikotnik1[0] in triangle:
            edge.append(trikotnik1[0])
            st = st + 1
        if trikotnik1[1] in triangle:
            edge.append(trikotnik1[1])
            st = st + 1
        if trikotnik1[2] in triangle:
            edge.append(trikotnik1[2])
            st = st + 1
        if st == 2:
            if (trikotnik1[0] in triangle) & (trikotnik1[2] in triangle):
                novi_edge = (edge[1], edge[0])
                sosedi.append((novi_edge, triangle))
            else:
                sosedi.append((edge, triangle))
        st = 0
        if sosedi:
            return sosedi[0][0], sosedi[0][1]
    return False


def delauneyPogoj(edge, sosed, trikotnik):
    pogoj = []
    for tocka in trikotnik:
        if not (tocka == edge[0] or tocka == edge[1]):
            t1 = tocka

    for tocka in sosed:
        if not (tocka == edge[0] or tocka == edge[1]):
            t2 = tocka

    if (angle(edge[0], t1, edge[1]) + angle(edge[0], t2, edge[1])) > np.pi + 0.0000001:
        pogoj.append((t1, t2, edge[0]))
        pogoj.append((t1, t2, edge[1]))
        return pogoj
    else:
        return False


def angle(A, B, C):
    BA = np.array([A[0] - B[0], A[1] - B[1]])
    BC = np.array([C[0] - B[0], C[1] - B[1]])
    kot_rad = np.arccos(np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC)))
    return kot_rad


def draw(trikotniki):
    plt.clf()
    for trikotnicek in trikotniki:
        seznamcek = list(trikotnicek)
        pts = np.array([list(seznamcek[0]), list(seznamcek[1]), list(seznamcek[2])])
        colors = np.random.rand(1, 3)
        p = Polygon(pts, facecolor=colors)
        ax = plt.gca()
        ax.add_patch(p)
        x = [seznamcek[0][0], seznamcek[1][0], seznamcek[2][0], seznamcek[0][0]]
        y = [seznamcek[0][1], seznamcek[1][1], seznamcek[2][1], seznamcek[0][1]]
        plt.plot(x, y, 'o', color='black')
        # plt.plot(x, y, color='black', linewidth=0.5)
    plt.show()


def optimize(T):
    draw(T)
    delauneyevi = T.copy()
    konec = False
    while not konec:
        konec = True
        sklad = delauneyevi.copy()
        delauneyevi = []
        while sklad:
            trikotnik = sklad.pop()
            if najdisoseda(trikotnik, sklad):
                edge, sosed = najdisoseda(trikotnik, sklad)
                pogoj = delauneyPogoj(edge, sosed, trikotnik)
                if pogoj:
                    konec = False
                    sklad.remove(sosed)
                    delauneyevi.append(pogoj[0])
                    delauneyevi.append(pogoj[1])
                else:
                    delauneyevi.append(trikotnik)
            else:
                delauneyevi.append(trikotnik)
    draw(delauneyevi)
    return delauneyevi


def test_examples(n):
    pointss = np.random.randint(100, size=(n, 2)).tolist()
    for i in range(len(pointss)):
        pointss[i] = tuple(pointss[i])
    return pointss


optimize(triangulate(test_examples(100))[1])
optimize(triangulate(test_examples(100), False)[1])
