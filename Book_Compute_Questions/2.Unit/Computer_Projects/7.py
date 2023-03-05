from random import randint


""" 
1. m X k matrix A ------ 2 X 3
2. k X n matrix B ------ 3 X 4

"""


def matrix_multi():
    A = [[randint(0, 5) for _ in range(3)] for _ in range(2)]
    B = [[randint(1, 6)for _ in range(4)] for _ in range(3)]
    for i in range(len(B)):
        try:
            print(f"{A[i]}\u0020\u0020{B[i]}")
        
        except IndexError:
            print(f"\t   {B[i]}")

# Complation need for first row first column calculation.


matrix_multi()
