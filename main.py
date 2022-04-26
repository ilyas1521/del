def ok(a):
    for x in range(1,10000000):
        # f = (¬ДЕЛ(x, 54) ∨ ¬ДЕЛ(x, 80)) → ¬ДЕЛ(x, A)
        f = (((x % 54) != 0) or ((x % 80) != 0)) <= ((x % a) != 0)
        if f == 0:
            return 0
    return 1

for a in range(1,100000):
    if ok(a):
        print(a)
        break
