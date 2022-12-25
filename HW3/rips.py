from itertools import combinations
import math
from collections import defaultdict


def conv_to_dict(VG, EG):
    G = {}
    for v in VG:
        G[v] = set()
    for (u, v) in EG:
        G[v].add(u)
        G[u].add(v)
    return G


def cliques(VG, EG, maximal=False):
    clique = []
    G = conv_to_dict(VG, EG)
    VG_set = set(VG)

    def tomita(R, P, X):
        if len(P) == 0 and len(X) == 0:
            clique.append(R)
            return
        # pivot
        unija = P.union(X)
        pivot = list(unija)[0]
        neighbours_of_pivot = G[pivot].intersection(P)
        for v in unija:
            neighbours_of_v = G[v].intersection(P)
            if G[v].intersection(P) > neighbours_of_pivot:
                neighbours_of_pivot = neighbours_of_v
                pivot = v

        for v in P.difference(neighbours_of_pivot):
            tomita(R.union({v}), P.intersection(G[v]), X.intersection(G[v]))
            P.remove(v)
            X.add(v)

    tomita(set(), VG_set, set())

    if maximal:
        return clique
    else:
        VRC = defaultdict(list)
        for mnozica in clique:
            seznam = list(mnozica)
            seznam.sort()
            for i in range(len(seznam)):
                seznamcek = list(combinations(seznam, i + 1))
                for element in seznamcek:
                    if element not in VRC[i]:
                        VRC[i].append(element)

        return dict(VRC)


def VR(S, epsilon):
    V = []
    E = []
    for i in range(len(S)):
        V.append(i)
    sorted_S = sorted(S, key=lambda z: z[0])
    for i in range(len(sorted_S)):
        for j in range(i + 1, len(sorted_S)):
            xi, yi = sorted_S[i]
            xj, yj = sorted_S[j]
            if abs(xj - xi) > epsilon:
                break
            elif math.sqrt((xj - xi) ** 2 + (yj - yi) ** 2) <= epsilon:
                E.append((S.index((xi, yi)), S.index((xj, yj))))

    return cliques(V, E)


test = cliques([1, 2, 3, 4, 5], [(1, 2), (1, 3), (2, 3), (2, 4), (4, 5), (3, 4), (1, 4), (5, 2)])
print(test)
test2 = VR([(0, 0), (1, 1), (2, 3), (-1, 2), (3, -1), (4, 2)], 3)
print(test2)
test3 = {}
test3[1] = "hehe"
# print(test3)
