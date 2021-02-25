"""       picked   pos=(pre+n-1) % len(arr)   n=2
A B C D E  B        1
A C D E    D        2
A C E      E        0
A C        A
(picked +n-1) % len(arr)
(picked +n-1) % len(arr)


"""


def share_cakes(names, n, pre=0):
    if names is None or len(names) == 0 or pre < 0:
        return None
    if len(names) == 1:
        return names[0]
    pos = (pre + n - 1) % len(names)
    popped = names.pop(pos)
    print(f"popped:{popped}, names:{names}")
    return share_cakes(names, n, pos)


print(share_cakes(['A', 'B', 'C', 'D', 'E'], 2))
