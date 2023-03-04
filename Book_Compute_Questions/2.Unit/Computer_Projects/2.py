
P = ['a' for _ in range(4)] \
    + ['b' for _ in range(1)] \
    + ['c' for _ in range(3)]


Q = ['a' for _ in range(3)] \
    + ['b' for _ in range(4)] \
    + ["d" for _ in range(2)]


def p_union_q():
    a_max = max(P.count("a"), Q.count("a"))
    b_max = max(P.count("b"), Q.count("b"))
    c_max = max(P.count('c'), Q.count("c"))
    d_max = max(P.count('d'), Q.count("d"))

    print(f'P \u222A Q = {{{a_max}.a, {b_max}.b, {c_max}.c, {d_max}.d}}')


p_union_q()


def p_intersec_q():
    a_min = min(P.count("a"), Q.count("a"))
    b_min = min(P.count("b"), Q.count("b"))
    c_min = min(P.count("c"), Q.count("c"))
    d_min = min(P.count("d"), Q.count("d"))

    print(f'P \u2229 Q = {{{a_min}.a, {b_min}.b, {c_min}.c, {d_min}.d}}')


p_intersec_q()


def p_dif_q():
    a_max_diff = max((P.count('a') - Q.count('a'), 0))
    b_max_diff = max((P.count('b') - Q.count('b'), 0))
    c_max_diff = max((P.count('c') - Q.count('c'), 0))
    d_max_diff = max((P.count('d') - Q.count('d'), 0))

    print(f'P \u2212 Q = {{{a_max_diff}.a, {b_max_diff}.b, {c_max_diff}.c, {d_max_diff}.d}}')

p_dif_q()


def p_sum_q():
    a_sum = P.count('a') + Q.count('a')
    b_sum = P.count('b') + Q.count('b')
    c_sum = P.count('c') + Q.count('c')
    d_sum = P.count('d') + Q.count('d')

    print(f'P \u002b Q = {{{a_sum}.a, {b_sum}.b, {c_sum}.c, {d_sum}.d}}')

p_sum_q()


