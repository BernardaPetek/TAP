import itertools
import unittest

def orientableQ(T):
    if orientable(T) is None:
        return False
    else:
        return True



def najdisosede(trikotnik1, T1):
    st = 0
    sosedi = []
    for triangle in T1:
        edge = []
        if trikotnik1[0] in triangle:
            edge.append(trikotnik1[0])
            st = st+1
        if trikotnik1[1] in triangle:
            edge.append(trikotnik1[1])
            st = st + 1
        if trikotnik1[2] in triangle:
            edge.append(trikotnik1[2])
            st = st + 1
        if st == 2:
            if (trikotnik1[0] in triangle) & (trikotnik1[2] in triangle):
                novi_edge = []
                novi_edge.append(edge[1])
                novi_edge.append(edge[0])
                sosedi.append((novi_edge, triangle))
            else:
                sosedi.append((edge, triangle))
        st = 0
    return sosedi

def sosedOrientiran(sosed1, orientirani1):
    st = 0
    for triangle in orientirani1:
        if sosed1[0] in triangle:
            st = st + 1
        if sosed1[1] in triangle:
            st = st + 1
        if sosed1[2] in triangle:
            st = st + 1
        if st == 3:
            return True
        st = 0
    return False

def zasukajTrikotnik(trikotnicek):
    najmanjsi = min(trikotnicek)
    indeks = trikotnicek.index(najmanjsi)
    if indeks == 0:
        return trikotnicek
    if indeks == 1:
        novi_tuple = (trikotnicek[1], trikotnicek[2], trikotnicek[0])
    if indeks == 2:
        novi_tuple = (trikotnicek[2], trikotnicek[0], trikotnicek[1])
    return novi_tuple

def orientable(T):
    sklad = []
    orientirani = []
    # sosede orientiraj tak da je najmanjsa st na prvem mestu
    taprvi = zasukajTrikotnik(T[0])
    orientirani.append(taprvi)
    sklad.append(taprvi)

    while sklad:
        trikotnik = sklad.pop()
        sosedi = najdisosede(trikotnik, T)
        for (edge,sosed) in sosedi:
            if sosedOrientiran(sosed, orientirani):
                #orientiraj soseda
                (a,b,c) = sosed
                if not(a == edge[1]) and not(a == edge[0]):
                    orientiran_sosed = (edge[1], edge[0],a)
                if not(b == edge[1]) and not(b == edge[0]):
                    orientiran_sosed = (edge[1], edge[0],b)
                if not(c == edge[1]) and not(c == edge[0]):
                    orientiran_sosed = (edge[1], edge[0],c)

                #napisi da je najmanjsa st na prvem mestu
                orientiran_sosed_novi = zasukajTrikotnik(orientiran_sosed)
                #a se sklada z orientiranimi
                if not (orientiran_sosed_novi in orientirani):
                    return None
                # ce se ne false
                #ce se ok good fino nic
            else:
                #orientiraj soseda
                (a, b, c) = sosed
                if not (a == edge[1]) and not (a == edge[0]):
                    orientiran_sosed1 = (edge[1], edge[0], a)
                if not (b == edge[1]) and not (b == edge[0]):
                    orientiran_sosed1 = (edge[1], edge[0], b)
                if not (c == edge[1]) and not (c == edge[0]):
                    orientiran_sosed1 = (edge[1], edge[0], c)

                sosed_novi =zasukajTrikotnik(orientiran_sosed1)
                sklad.append(sosed_novi)
                orientirani.append(sosed_novi)

    return orientirani



class TestOrinetable(unittest.TestCase):
    def test_testcase1(self):
        M = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (2, 5, 6), (1, 2, 6)]
        result = orientableQ(M)
        expected = False
        self.assertEqual(result, expected)

    def test_testcase2(self):
        M = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (2, 5, 6), (1, 2, 6)]
        result = orientable(M)
        expected = None
        self.assertEqual(result, expected)

    def test_testcase3(self):
        M = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
        result = orientable(M)
        expected = [(1, 2, 3), (1, 4, 2), (1, 3, 4), (2, 4, 3)]
        self.assertEqual(result, expected)

    def test_testcase4(self):
        M = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
        result = orientableQ(M)
        expected = True
        self.assertEqual(result, expected)

    #torus
    def test_testcase5(self):
        torus = [(1,2,5),(2,5,6),(2,3,6),(1,3,7),(3,6,7),(5,7,1),(5,4,6),(4,6,8),(6,7,8),(7,8,9),(7,5,9),(5,4,9),(1,4,8),(8,1,2),(2,8,9),(9,2,3),(4,9,3),(4,3,1)]
        result = orientableQ(torus)
        expected = True
        self.assertEqual(result, expected)

    def test_testcase6(self):
        torus = [(1,2,5),(2,5,6),(2,3,6),(1,3,7),(3,6,7),(5,7,1),(5,4,6),(4,6,8),(6,7,8),(7,8,9),(7,5,9),(5,4,9),(1,4,8),(8,1,2),(2,8,9),(9,2,3),(4,9,3),(4,3,1)]
        result = orientable(torus)
        expected = [(1, 2, 5), (2, 6, 5), (1, 5, 7), (1, 8, 2), (1, 4, 8), (2, 8, 9), (7, 9, 8), (2, 9, 3), (2, 3, 6), (3, 9, 4), (4, 9, 5), (1, 3, 4), (1, 7, 3), (3, 7, 6), (6, 7, 8), (4, 6, 8), (4, 5, 6), (5, 9, 7)]
        self.assertEqual(result, expected)

    #klein bottle
    def test_testcase7(self):
        kleinbottle = [(1,2,4),(2,4,6),(2,3,6),(1,3,7),(3,6,7),(5,7,1),(5,4,6),(5,6,8),(6,7,8),(7,8,9),(7,5,9),(5,4,9),(1,5,8),(8,1,2),(2,8,9),(9,2,3),(4,9,3),(4,3,1)]
        result = orientableQ(kleinbottle)
        expected = False
        self.assertEqual(result, expected)

    def test_testcase8(self):
        kleinbottle = [(1,2,4),(2,4,6),(2,3,6),(1,3,7),(3,6,7),(5,7,1),(5,4,6),(5,6,8),(6,7,8),(7,8,9),(7,5,9),(5,4,9),(1,5,8),(8,1,2),(2,8,9),(9,2,3),(4,9,3),(4,3,1)]
        result = orientable(kleinbottle)
        expected = None
        self.assertEqual(result, expected)

    #sphere
    def test_testcase9(self):
        sphere = [(1, 2, 4), (1,2,3),(3,2,4),(1,3,4)]
        result = orientableQ(sphere)
        expected = True
        self.assertEqual(result, expected)
        # sphere

    def test_testcase10(self):
        sphere = [(1, 2, 4), (1, 2, 3), (3, 2, 4), (1, 3, 4)]
        result = orientable(sphere)
        expected = [(1, 2, 4), (1, 3, 2), (2, 3, 4), (1, 4, 3)]
        self.assertEqual(result, expected)

    #cylinder
    def test_testcase11(self):
        cylinder = [(1,4,6),(1,6,2),(2,5,6),(2,3,5),(3,4,5),(1,3,4)]
        result = orientableQ(cylinder)
        expected = True
        self.assertEqual(result, expected)

    def test_testcase12(self):
        cylinder = [(1, 4, 6), (1, 6, 2), (2, 5, 6), (2, 3, 5), (3, 4, 5), (1, 3, 4)]
        result = orientable(cylinder)
        expected = [(1, 4, 6), (1, 6, 2), (1, 3, 4), (3, 5, 4), (2, 5, 3), (2, 6, 5)]
        self.assertEqual(result, expected)

    #moebiusband
    def test_testcase13(self):
        moebiusband = [(1,2,4),(1,3,4),(3,4,6),(3,5,6),(5,6,8),(5,7,8),(7,8,1),(1,2,7)]
        result = orientableQ(moebiusband)
        expected = False
        self.assertEqual(result, expected)

    def test_testcase14(self):
        moebiusband = [(1,2,4),(1,3,4),(3,4,6),(3,5,6),(5,6,8),(5,7,8),(7,8,1),(1,2,7)]
        result = orientable(moebiusband)
        expected = None
        self.assertEqual(result, expected)



if __name__ == '__main__':
    print("Testing examples")
    unittest.main()

