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

    result = [] # final result
    for i in range(len(A)):

        row = [] # the new row in new matrix
        for j in range(len(B[0])):
            item = 0 # the new element in the new row
            for v in range(len(A[i])):
                item += A[i][v] * B[v][j]
            row.append(item) # append sum of product into the new row
        
        result.append(row) # append the new row into the final result

    for i in range(len(result)):
        print(f"{result[i]}")


# Index Error on B

# print(f'{A[0][0]*B[0][3] + A[0][1]*B[1][3] + A[0][2]*B[2][3]}')
# Complation need for first row first column calculation.
matrix_multi()
