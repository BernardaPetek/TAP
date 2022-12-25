import math
import random
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from linesweeptriangulation import triangulate
from scipy import linalg


def delauney_condition(triangle1: set, triangle2: set):
    intersect_list = list(triangle1.intersection(triangle2))
    set1 = set(triangle1.difference(triangle2))
    set2 = set(triangle2.difference(triangle1))
    tocka1 = set1.pop()
    tocka2 = set2.pop()
    if (angle(intersect_list[0], tocka1, intersect_list[1]) + angle(intersect_list[0], tocka2,
                                                                    intersect_list[1])) > np.pi+0.00001:
        return True
    else:
        return False


def angle(A, B, C):
    BA = np.array([A[0] - B[0], A[1] - B[1]])
    BC = np.array([C[0] - B[0], C[1] - B[1]])
    kot_rad = np.arccos(np.dot(BA, BC) / (linalg.norm(BA) * linalg.norm(BC)))
    return round(kot_rad,6)


def draw(trikotniki):
    for trikotnicek in trikotniki:
        seznamcek = list(trikotnicek)
        pts = np.array([list(seznamcek[0]), list(seznamcek[1]), list(seznamcek[2])])
        colors = np.random.rand(1, 3)
        p = Polygon(pts, facecolor=colors, linewidth=0.1, edgecolor=None)
        ax = plt.gca()
        ax.add_patch(p)
        ax.axis("equal")
        x = [seznamcek[0][0], seznamcek[1][0], seznamcek[2][0], seznamcek[0][0]]
        y = [seznamcek[0][1], seznamcek[1][1], seznamcek[2][1], seznamcek[0][1]]
        plt.plot(x, y, 'o', color='black');
        # plt.plot(x, y, color='black', linewidth=0.5);
    plt.show()


def test_examples(n):
    pointss = np.random.randint(500, size=(n, 2)).tolist()
    for i in range(len(pointss)):
        pointss[i] = tuple(pointss[i])
    return pointss


def optimize(T):
    draw(T)
    T1 = set()
    not_delauney = True
    for i in range(len(T)):
        T1.add(frozenset(T[i]))
    while not_delauney:
        edge_flip = []
        not_delauney = False
        for triangle1 in T1:
            for triangle2 in T1:
                if len(triangle1.intersection(triangle2)) == 2:
                    if delauney_condition(triangle1, triangle2):
                        edge_flip = [triangle1, triangle2]
                        not_delauney = True
                        break
            if edge_flip:
                break
        if edge_flip:
            T1.remove(edge_flip[0])
            T1.remove(edge_flip[1])

            intersection_list = []
            set1 = set(edge_flip[0].intersection(edge_flip[1]))

            intersection_list.append(set1.pop())
            intersection_list.append(set1.pop())

            new_set_1 = set(edge_flip[0].symmetric_difference(edge_flip[1]))
            new_set_2 = set(edge_flip[1].symmetric_difference(edge_flip[0]))

            new_set_1.add(intersection_list[0])
            new_set_2.add(intersection_list[1])

            T1.add(frozenset(new_set_1))
            T1.add(frozenset(new_set_2))

    draw(T1)
    return T1


# optimize([((0.1, 0.1), (5, -1), (7, -5)), ((5, -1), (7, -5), (9, 4)), ((0.1, 0.1), (5, -1), (9, 4)), ((0.1, 0.1), (3, 9), (9, 4))])

#a = triangulate(test_examples(100))
#for i in range(len(a)):
    #a[i] = (((round(a[i][0][0],3), round(a[i][0][1],3))),((round(a[i][1][0],3), round(a[i][1][1],3))),((round(a[i][2][0],3), round(a[i][2][1],3))))

#optimize(a)
optimize(triangulate(test_examples(100))[1])
