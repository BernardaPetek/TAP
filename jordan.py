def collinear_points(A, B, C):
    determinant = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    if determinant == 0:
        return True
    else:
        return False


def lies_on_segment(A, B, C):
    t = (A[1] - B[1]) / (C[1] - B[1])
    s = B[0] - A[0] + t * (C[0] - B[0])

    if 0 <= t <= 1:
        return True
    else:
        return False


# rotacija okoli centra ki je nasa tocka T
def rotate_curve():
    print("whaaat")
    return []


def insideQ(P, T):
    # all lines
    P1 = P.copy()
    P1.append(P[0])
    rotate = True

    while rotate:
        rotate = False
        P2 = []
        for i in range(len(P1) - 1):
            if collinear_points(T, P1[i], P1[i + 1]):
                if lies_on_segment(T, P1[i], P1[i + 1]):
                    return True
                elif P[i][0] > T[0] and P[i][1] == T[1] and P[i+1][1] == T[1]:
                    rotate = True
                    P2 = rotate_curve()
                # ce lezi na krivulji potem vrni true v splosnem drugac pa rotiraj
        if len(P2) != 0:
            P1 = P2.copy()

    # prestej kolkokrat seka
    number_of_intersections = 0
    for i in range(len(P1) - 1):
        t = (T[1] - P1[i][1]) / (P1[i + 1][1] - P1[i][1])
        s = P1[i][0] - T[0] + t * (P1[i + 1][0] - P1[i][0])

        if s > 0 and 0 < t < 1:
            number_of_intersections += 1
        elif s > 0 and t == 1:
            if i == len(P1) - 2:
                if not(((P1[i][1] > P1[i + 1][1] and P1[1][1] > P1[i + 1][1])) or ( (
                        P1[i][1] < P1[i + 1][1] and P1[1][1] < P1[i + 1][1]))):
                    number_of_intersections += 1
            else:
                if not(( (P1[i][1] > P1[i + 1][1] and P1[i + 2][1] > P1[i + 1][1])) or (
                (P1[i][1] < P1[i + 1][1] and P1[i + 2][1] < P1[i + 1][1]))):
                    number_of_intersections += 1

    if number_of_intersections % 2 == 0:
        return False
    else:
        return True


print(insideQ([(0.02, 0.10), (0.98, 0.05), (2.10, 1.03), (3.11, -1.23), (4.34, -0.35),
               (4.56, 2.21), (2.95, 3.12), (2.90, 0.03), (1.89, 2.22)], (2.33, 0.66)))

# seka enkrat
print(insideQ([(2, 1), (2, 0), (1, -1), (0, 0), (0, 1), (1, 2)], (1, 1)))
# seka enkrat skoz tocko
print(insideQ([(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)], (1, 1)))
# lezi na tocki
print(insideQ([(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)], (1, -1)))
# lezi na segmentu line
print(insideQ([(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)], (0, 0.5)))

# seka skoz tocko ko ni kul - zmisli primer, ko ne rabi rotacije - lezi zunaj!
print(insideQ([(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)], (0, 2)))

# primer z rotacijo

# lezi zunaj
print(insideQ([(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)], (0, 3)))

# lezi zunaj seka dvakrat
print(insideQ([(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)], (-1, 0.5)))
