import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def intersection(A, B, C, D):
    if -1e-8 < ((B[0] - A[0]) * (D[1] - C[1]) - (D[0] - C[0]) * (B[1] - A[1])) < 1e-8:
        k = (((C[0] - A[0]) * (D[1] - C[1])) - ((C[1] - A[1]) * (D[0] - C[0]))) / 1e-8
    else:
        k = (((C[0] - A[0]) * (D[1] - C[1])) - ((C[1] - A[1]) * (D[0] - C[0]))) / (
                (B[0] - A[0]) * (D[1] - C[1]) - (D[0] - C[0]) * (B[1] - A[1]))
        l = (A[0] + k * (B[0] - A[0]) - C[0]) / (D[0] - C[0])

    if 0 < round(k, 8) < 1 and 0 < round(l, 8) < 1:
        return True
    return False


def generify(S):
    S1 = S.copy()
    mu, sigma = 0, 0.2
    for i in range(len(S)):
        s = np.random.normal(mu, sigma)
        s1 = np.random.normal(mu, sigma)
        S1[i] = (S[i][0] + s, S[i][1] + s1)
    return S1


def draw(V, E):
    plt.clf()
    triangulation = []
    for (a, b) in E:
        for v in V:
            if (((a, v) in E) or ((v, a) in E)) and (((b, v) in E) or ((v, b) in E)):
                nejapendam = True
                for (bla, bli, ble) in triangulation:
                    if ((a == bla) and (b == bli) and (v == ble)) or ((a == bla) and (v == bli) and (b == ble)):
                        nejapendam = False
                        break
                    if ((b == bla) and (a == bli) and (v == ble)) or ((b == bla) and (v == bli) and (a == ble)):
                        nejapendam = False
                        break
                    if ((v == bla) and (a == bli) and (b == ble)) or ((v == bla) and (b == bli) and (a == ble)):
                        nejapendam = False
                        break
                if nejapendam:
                    triangulation.append((a, b, v))

                pts = np.array([list(a), list(b), list(v)])
                colors = np.random.rand(1, 3)
                p = Polygon(pts, facecolor=colors)
                ax = plt.gca()
                ax.add_patch(p)
                x = [a[0], b[0], v[0], a[0]]
                y = [a[1], b[1], v[1], a[1]]
                plt.plot(x, y, 'o', color='black')
                plt.plot(x, y, color='black', linewidth=0.5)
    plt.show()

    return triangulation


def triangulate(S, vertical=True):
    # tocke po vrsti za vetical
    if vertical:
        events = sorted(S, key=lambda z: z[0])
    else:
        events = sorted(S, key=lambda z: z[1])

    # edges ki so ze v trangulaciji
    edges_in = []
    points_in = set()
    S_generified = generify(events)
    add_edge = True
    for point in S_generified:
        for point1 in points_in:
            for (c, d) in edges_in:
                if intersection(point, point1, c, d):
                    add_edge = False
            if add_edge:
                if (not ((point1, point) in edges_in)) and (not ((point, point1) in edges_in)):
                    edges_in.append((point, point1))
            add_edge = True
        points_in.add(point)
    triangulation1 = draw(set(S_generified), edges_in)
    return edges_in, triangulation1


def test_examples(n, seed):
    np.random.seed(seed)
    pointss = np.random.randint(100, size=(n, 2)).tolist()
    for i in range(len(pointss)):
        pointss[i] = tuple(pointss[i])
    return pointss


if __name__ == '__main__':
    triangulate([(0, 0), (3, 9), (5, -1), (9, 4), (7, -5)])
    triangulate([(0, 0), (3, 9), (5, -1), (9, 4), (7, -5)], vertical=False)
    triangulate(test_examples(100, 0))
    triangulate(test_examples(100, 0), vertical=False)
    triangulate(test_examples(100, 1))
    triangulate(test_examples(100, 1), vertical=False)
