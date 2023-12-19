for a in range(5):
    inner_loop_broke = False
    for b in range(1000):
        if b > 1:
            inner_loop_broke = True
            continue
        print(a, b)
    if inner_loop_broke:
        continue
    print(a)
