from random import randint
N = {1,2,3,4,5,6,7,8,9}

A = {0,1,2,3,4}
B = {2,3,4,5,6,7,8,9,10}

A_complement = {i for i in N if i not in A}
print(f"Complement: {A_complement}")

A_U_B = A | B
print(f"Union: {A_U_B}")

A_Intersection_B = {i for i in A if i in B}
print(f"Intersection: {A_Intersection_B}")

A_dif_B = {i for i in A if i not in B}
print(f"Diff: {A_dif_B}")

A_xor_B = A ^ B
print(f"{A_xor_B}")




#n = {randint(1,10) for _ in range(10)}

#print(n)