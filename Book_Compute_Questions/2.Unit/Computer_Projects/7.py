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

    for i in A[0][1]:
        print(i)


# print(f'{A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0]}')
# Complation need for first row first column calculation.


matrix_multi()
