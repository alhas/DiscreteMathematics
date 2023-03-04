from random import random

animals = ['cat', 'dog', 'bird', 'lion', 'tiger',
           'elephant', 'giraffe', 'monkey', 'snake', 'zebra']

fruits = ['apple', 'banana', 'orange', 'kiwi', 'mango',
          'pineapple', 'strawberry', 'grapefruit', 'pear', 'watermelon']

A = {animal: random() for animal in animals}
F = {fruit: random() for fruit in fruits}

A_complement = {key: 1 - value for key, value in A.items()}
# A complement
print(sorted(A_complement.items()))

# F complement
F_complement = {key: 1 - value for key, value in F.items()}
print(sorted(F_complement.items()))


def a_union_f(set1: dict, set2: dict):
    fuzzy_union_set_1 = max(set1, key=set1.get)
    fuzzy_union_set_2 = max(set2, key=set2.get)

    print(f"Strongest: {fuzzy_union_set_1}")
    print(f"Sweetest: {fuzzy_union_set_2}\n")


a_union_f(A, F)


def a_intersec_f(set1: dict, set2: dict):
    fuzzy_union_set_1 = min(set1, key=set1.get)
    fuzzy_union_set_2 = min(set2, key=set2.get)

    print(f"Weakest: {fuzzy_union_set_1}")
    print(f"Sweetest: {fuzzy_union_set_2}")


a_intersec_f(A, F)
