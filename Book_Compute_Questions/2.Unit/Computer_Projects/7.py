from random import randint


"""
1. m X k matrix A ------ 2 X 3
2. k X n matrix B ------ 3 X 4

"""


def matrix_multi():
    A = [[randint(0, 5) for _ in range(3)] for _ in range(2)]
    B = [[randint(1, 6) for _ in range(4)] for _ in range(3)]
    for i in range(len(B)):
        try:
            print(f"{A[i]}\u0020\u0020{B[i]}")

        except IndexError:
            print(f"\t   {B[i]}")
    value_a = list()
    value_b = list()
    index_a = 0
    for row in A:
        for x in range(len(row)):
            value_a.append(A[index_a][x])
        index_a += 1

    for column in range(len(B[0])):
        for i in range(len(B)):
            # value_b = B[i][index_b]
            value_b.append(B[i][column])

    print(value_a, value_b)




# Index Error on B

# print(f'{A[0][0]*B[0][3] + A[0][1]*B[1][3] + A[0][2]*B[2][3]}')
# Complation need for first row first column calculation.


matrix_multi()
