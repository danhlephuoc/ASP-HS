input = """
1 2 2 1 3 4
1 3 2 1 2 4
1 4 0 0
1 5 2 1 6 7
1 6 2 1 5 7
1 7 0 0
1 8 2 1 9 10
1 9 2 1 8 10
1 10 0 0
1 11 2 1 12 13
1 12 2 1 11 13
1 13 0 0
1 14 2 1 15 16
1 15 2 1 14 16
1 16 0 0
1 17 2 1 18 19
1 18 2 1 17 19
1 19 0 0
1 20 1 0 2
1 21 1 0 14
1 22 2 0 21 11
1 21 2 0 22 11
1 23 2 0 20 8
1 24 2 0 23 5
1 23 2 0 24 5
1 20 2 0 23 8
1 1 1 1 23
1 1 1 1 22
1 1 2 0 17 5
1 1 2 0 11 2
1 1 2 0 5 17
1 1 2 0 2 11
1 1 2 0 2 14
1 1 2 0 14 2
1 1 2 0 5 14
1 1 2 0 8 11
1 1 2 0 11 8
1 1 2 0 14 5
1 1 2 0 17 8
1 1 2 0 8 17
1 1 2 0 22 20
1 1 2 0 20 22
1 25 2 1 24 5
1 25 2 1 20 8
1 25 2 1 23 5
1 25 2 1 23 8
1 25 2 1 21 11
1 25 2 1 22 11
1 26 1 0 17
1 27 1 0 14
1 28 1 0 11
1 29 1 0 8
1 26 1 0 5
1 28 1 0 2
0
12 nol5
20 r1
24 r2
2 l1
8 l4
11 l5
3 nol1
18 nol7
23 r6
9 nol4
5 l3
17 l7
26 link(e0111)
27 link(e0001)
28 link(e0010)
29 link(e1011)
22 r5
25 pippo
15 nol6
14 l6
21 r4
6 nol3
0
B+
0
B-
1
0
1
"""
output = """
"""
