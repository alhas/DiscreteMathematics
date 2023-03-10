from random import randint

"""
1. m X k matrix A ------ 2 X 3
2. k X n matrix B ------ 3 X 4
"""


def matrix_multi():
    A = [[randint(0, 9) for _ in range(3)] for _ in range(2)]
    B = [[randint(0, 9) for _ in range(4)] for _ in range(3)]
    for i_row in range(len(B)):
        try:
            print(f"{A[i_row]}\u0020\u0020{B[i_row]}")

        except IndexError:
            print(f"\t   {B[i_row]}")
    value_a = int()
    value_b = int()

    for x_row in range(len(A)):
        for x_column in range(len(A[0])):
            value_a = A[x_row][x_column]
    for y_column in range(len(B[0])):
        for i_row in range(len(B)):
            value_b = B[i_row][y_column]

    print(value_a, value_b)


# Index Error on B

# print(f'{A[0][0]*B[0][3] + A[0][1]*B[1][3] + A[0][2]*B[2][3]}')
# Complation need for first row first column calculation.
matrix_multi()
