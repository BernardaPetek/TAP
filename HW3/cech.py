import math
from random import randrange, randint
from rips import VR


def lies_in_circle(tocka, krog):
    e, f = tocka
    if len(krog) == 0:
        return False
    if len(krog) == 1:
        a, b = krog[0]
        c, d = tocka
        return a == c and b == d
    if len(krog) == 2:
        a, b = krog[0]
        c, d = krog[1]
        return (e - ((a + c) / 2)) ** 2 + (f - ((b + d) / 2)) ** 2 <= (math.dist(krog[0], krog[1]) / 2) ** 2
    if len(krog) == 3:
        ax, ay = krog[0]
        bx, by = krog[1]
        cx, cy = krog[2]
        bx_trans, by_trans = bx - ax, by - ay
        cx_trans, cy_trans = cx - ax, cy - ay
        d = 2 * (bx_trans * cy_trans - by_trans * cx_trans)
        ux_trans = (1 / d) * (cy_trans * (bx_trans ** 2 + by_trans ** 2) - by_trans * (cx_trans ** 2 + cy_trans ** 2))
        uy_trans = (1 / d) * (bx_trans * (cx_trans ** 2 + cy_trans ** 2) - cx_trans * (bx_trans ** 2 + by_trans ** 2))
        ux = ux_trans + ax
        uy = uy_trans + ay
        center = [ux, uy]
        return (e - ux) ** 2 + (f - uy) ** 2 <= math.dist(center, krog[0]) ** 2


def welzl(P, R):
    P = list(P)
    R = list(R)
    if not P or len(R) == 3:
        return R
    idx = randint(0, len(P) - 1)
    p = P.pop(idx)
    D = welzl(P, R)
    if lies_in_circle(p, D):
        return D
    R.append(p)
    return welzl(P, R)


def izracunaj_polmer(seznam_tock):
    if len(seznam_tock) == 2:
        return (math.dist(seznam_tock[0], seznam_tock[1]) / 2)

    ax, ay = seznam_tock[0]
    bx, by = seznam_tock[1]
    cx, cy = seznam_tock[2]
    bx_trans, by_trans = bx - ax, by - ay
    cx_trans, cy_trans = cx - ax, cy - ay
    d = 2 * (bx_trans * cy_trans - by_trans * cx_trans)
    ux_trans = (1 / d) * (cy_trans * (bx_trans ** 2 + by_trans ** 2) - by_trans * (cx_trans ** 2 + cy_trans ** 2))
    uy_trans = (1 / d) * (bx_trans * (cx_trans ** 2 + cy_trans ** 2) - cx_trans * (bx_trans ** 2 + by_trans ** 2))
    ux = ux_trans + ax
    uy = uy_trans + ay
    center = [ux, uy]
    return math.dist(center, seznam_tock[0])


def cech(S, epsilon):
    spimpan_rips_complex = VR(S, 2 * epsilon)
    print(spimpan_rips_complex)
    dolzina = len(spimpan_rips_complex)
    for i in range(2, dolzina):
        za_izbris = []
        for element in spimpan_rips_complex[i]:
            novi_S = []
            for j in element:
                novi_S.append(S[j])
            if izracunaj_polmer(welzl(novi_S, [])) > epsilon:
                za_izbris.append(element)
        for elementek in za_izbris:
            spimpan_rips_complex[i].remove(elementek)

    return spimpan_rips_complex


# print(welzl([(0, 0), (0, 1), (1, 0)], []))
# print(welzl([(5, -2), (-3, -2), (-2, 5), (1, 6), (0, 2)], []))
S = [(-2, 1), (-2, -2), (1, -1), (1.5, 2.5)]
print("testiiirammmm")
print(cech(S, 2))
