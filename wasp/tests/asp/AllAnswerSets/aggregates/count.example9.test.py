input = """
1 2 3 2 3 4 5
1 3 3 2 2 4 5
1 4 3 2 2 3 5
1 5 0 0
1 6 3 2 7 8 9
1 7 3 2 6 8 9
1 8 3 2 6 7 9
1 9 0 0
1 10 3 2 11 12 13
1 11 3 2 10 12 13
1 12 3 2 10 11 13
1 13 0 0
1 14 1 0 4
1 15 1 0 3
1 16 1 0 2
1 17 1 0 8
1 18 1 0 7
1 19 1 0 6
2 21 3 0 1 16 15 14
1 20 1 0 21
2 23 3 0 1 16 15 14
2 24 3 0 3 16 15 14
1 22 2 1 24 23
2 26 3 0 1 19 18 17
1 25 1 0 26
2 28 3 0 1 12 11 10
1 27 1 0 28
0
25 okay2
14 a(3)
15 a(2)
16 a(1)
20 okay
27 okay3
10 e(1)
11 e(2)
12 e(3)
6 d(1)
7 d(2)
8 d(3)
17 b(3)
18 b(2)
19 b(1)
22 okay1
2 c(1)
3 c(2)
4 c(3)
0
B+
0
B-
1
0
1
"""
output = """
{c(1), d(1), e(1), a(1), b(1), okay, okay1, okay2, okay3}
{c(1), d(1), e(2), a(1), b(1), okay, okay1, okay2, okay3}
{c(1), d(1), e(3), a(1), b(1), okay, okay1, okay2, okay3}
{c(1), d(2), e(1), a(1), b(2), okay, okay1, okay2, okay3}
{c(1), d(2), e(2), a(1), b(2), okay, okay1, okay2, okay3}
{c(1), d(2), e(3), a(1), b(2), okay, okay1, okay2, okay3}
{c(1), d(3), e(1), a(1), b(3), okay, okay1, okay2, okay3}
{c(1), d(3), e(2), a(1), b(3), okay, okay1, okay2, okay3}
{c(1), d(3), e(3), a(1), b(3), okay, okay1, okay2, okay3}
{c(2), d(1), e(1), a(2), b(1), okay, okay1, okay2, okay3}
{c(2), d(1), e(2), a(2), b(1), okay, okay1, okay2, okay3}
{c(2), d(1), e(3), a(2), b(1), okay, okay1, okay2, okay3}
{c(2), d(2), e(1), a(2), b(2), okay, okay1, okay2, okay3}
{c(2), d(2), e(2), a(2), b(2), okay, okay1, okay2, okay3}
{c(2), d(2), e(3), a(2), b(2), okay, okay1, okay2, okay3}
{c(2), d(3), e(1), a(2), b(3), okay, okay1, okay2, okay3}
{c(2), d(3), e(2), a(2), b(3), okay, okay1, okay2, okay3}
{c(2), d(3), e(3), a(2), b(3), okay, okay1, okay2, okay3}
{c(3), d(1), e(1), a(3), b(1), okay, okay1, okay2, okay3}
{c(3), d(1), e(2), a(3), b(1), okay, okay1, okay2, okay3}
{c(3), d(1), e(3), a(3), b(1), okay, okay1, okay2, okay3}
{c(3), d(2), e(1), a(3), b(2), okay, okay1, okay2, okay3}
{c(3), d(2), e(2), a(3), b(2), okay, okay1, okay2, okay3}
{c(3), d(2), e(3), a(3), b(2), okay, okay1, okay2, okay3}
{c(3), d(3), e(1), a(3), b(3), okay, okay1, okay2, okay3}
{c(3), d(3), e(2), a(3), b(3), okay, okay1, okay2, okay3}
{c(3), d(3), e(3), a(3), b(3), okay, okay1, okay2, okay3}
"""
