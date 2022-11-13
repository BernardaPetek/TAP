import math
import unittest

def collinear_points(A, B, C):
    determinant = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    if determinant == 0:
        return True
    else:
        return False


def lies_on_segment(A, B, C):
    segment3 = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2)
    segment2 = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
    segment1 = math.sqrt((C[0] - A[0])**2 + (C[1] - A[1])**2)

    if segment1 + segment2 == segment3:
        return True
    else:
        return False


# rotacija okoli centra ki je nasa tocka T
def rotate_curve(P, T, angle):
    P1 = []
    angle1 = math.radians(angle)
    for (a, b) in P:
        P1.append(((math.cos(angle1) * a - T[0] - math.sin(angle1) * b - T[1]) + T[0],
                  (math.sin(angle1) * a - T[0] + math.cos(angle1) * b - T[1]) + T[1]))
    return P1


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
                # rotiraj samo ce so kolinearne na desno
                elif P[i][0] > T[0] and P[i][1] == T[1] and P[i + 1][1] == T[1]:
                    rotate = True
                    P2 = rotate_curve(P1, T, 25)
        if len(P2) != 0:
            P1 = P2.copy()

    # prestej kolkokrat seka
    number_of_intersections = 0
    for i in range(len(P1) - 1):
        if (P1[i + 1][1] - P1[i][1]) != 0:
            t = (T[1] - P1[i][1]) / (P1[i + 1][1] - P1[i][1])
            s = P1[i][0] - T[0] + t * (P1[i + 1][0] - P1[i][0])

            if s > 0 and 0 < t < 1:
                number_of_intersections += 1
            elif s > 0 and t == 1:
                if i == len(P1) - 2:
                    if not (((P1[i][1] > P1[i + 1][1] and P1[1][1] > P1[i + 1][1])) or ((
                            P1[i][1] < P1[i + 1][1] and P1[1][1] < P1[i + 1][1]))):
                        number_of_intersections += 1
                else:
                    if not (((P1[i][1] > P1[i + 1][1] and P1[i + 2][1] > P1[i + 1][1])) or (
                            (P1[i][1] < P1[i + 1][1] and P1[i + 2][1] < P1[i + 1][1]))):
                        number_of_intersections += 1

    if number_of_intersections % 2 == 0:
        return False
    else:
        return True



class TestGraphComponents(unittest.TestCase):
    def test_testcase1(self):
        P = [(0.02, 0.10), (0.98, 0.05), (2.10, 1.03), (3.11, -1.23), (4.34, -0.35),
               (4.56, 2.21), (2.95, 3.12), (2.90, 0.03), (1.89, 2.22)]
        T = (2.33, 0.66)
        result = insideQ(P, T)
        expected = True
        self.assertEqual(result, expected)

    #seka enkrat
    def test_testcase2(self):
        P = [(2, 1), (2, 0), (1, -1), (0, 0), (0, 1), (1, 2)]
        T = (1,1)
        result = insideQ(P, T)
        expected = True
        self.assertEqual(result, expected)

    #seka skoz tocko
    def test_testcase3(self):
        P = [(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)]
        T = (1, 1)
        result = insideQ(P, T)
        expected = True
        self.assertEqual(result, expected)

    #lezi na krivulji na tocki
    def test_testcase4(self):
        P = [(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)]
        T = (1, -1)
        result = insideQ(P, T)
        expected = True
        self.assertEqual(result, expected)

    #lezi na krivulji na line segmentu
    def test_testcase5(self):
        P = [(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)]
        T = (0, 0.5)
        result = insideQ(P, T)
        expected = True
        self.assertEqual(result, expected)

    #ne lezi na krivulji in seka tocko
    def test_testcase6(self):
        P = [(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)]
        T = (0, 2)
        result = insideQ(P, T)
        expected = False
        self.assertEqual(result, expected)

    #lezi noter ampak je treba rotirat
    def test_testcase7(self):
        P = [(2, 0), (0, 0), (0, 1), (1, 2), (1, 1), (2, 1)]
        T = (0.5, 1)
        result = insideQ(P, T)
        expected = True
        self.assertEqual(result, expected)

    #lezi zunaj
    def test_testcase8(self):
        P = [(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)]
        T = (0, 3)
        result = insideQ(P, T)
        expected = False
        self.assertEqual(result, expected)

    #lezi zunaj in seka dvakrat
    def test_testcase8(self):
        P = [(2, 0), (1, -1), (0, 0), (0, 1), (1, 2), (2, 1)]
        T = (-1, 0.5)
        result = insideQ(P, T)
        expected = False
        self.assertEqual(result, expected)

    #lezi zunaj in je treba rotirat
    def test_testcase9(self):
        P = [(2, 0), (0, 0), (0, 1), (1, 2), (1, 1), (2, 1)]
        T = (3, 1)
        result = insideQ(P, T)
        expected = False
        self.assertEqual(result, expected)





if __name__ == '__main__':
    print("Testing examples")
    unittest.main()






