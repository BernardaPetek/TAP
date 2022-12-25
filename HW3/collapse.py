from itertools import combinations


def collapse(X, progress=True):
    mnozica_vseh = X.copy()
    collapsible = True
    while collapsible:
        simplex_face = []
        simplex_face_free = []
        collapsible = False
        for simplex in mnozica_vseh:
            seznamcek = list(combinations(simplex, len(simplex) - 1))
            element = (simplex, seznamcek)
            simplex_face.append(element)

        for a, b in simplex_face:
            proste_faces = []
            for i in range(0, len(b)):
                j = 0
                for c, d in simplex_face:
                    mnozica = set(c)
                    mnozica2 = set(b[i])
                    if len(mnozica2.intersection(mnozica)) == len(mnozica2):
                        j = j + 1
                if j == 1:
                    proste_faces.append(b[i])
            simplex_face_free.append((a, proste_faces))

        for a, b in simplex_face_free:
            if len(b) and len(b[0]):
                collapsible = True
                mnozica_vseh.remove(a)
                for i in range(1, len(b)):
                    mnozica_vseh.append(b[i])
                break

    return mnozica_vseh


# primer = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
# print(collapse(primer))
# primer2 = [(1, 2, 3), (2, 3, 5), (3, 4), (5, 6)]
# print(collapse(primer2))
primer3 = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (1, 5, 6), (1, 2, 6)]
print(collapse(primer3))
# primer4 = [(0, 3, 5), (1, 4, 5), (2, 3), (2, 4), (3, 4)]
# print(collapse(primer4))
# primer5 = [(0, 3, 5), (1, 4, 5), (2, 3, 4)]
# print(collapse(primer5))
