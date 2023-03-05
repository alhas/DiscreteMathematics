def is_one_to_one(f,n):
    range_set = set()
    for i in range(1, n+1):
        fi = f(i)
        if fi in range_set:
            return False
        range_set.add(fi)
        print(fi)
    return True

def f(x):
    return 2*x


print(is_one_to_one(f,5))