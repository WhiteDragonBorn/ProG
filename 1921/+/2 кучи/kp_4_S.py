# 1921 --- 4 --- KP

from functools import lru_cache
trg = 53
def movs(h):
    a,b = h
    return (a+1,b), (a,b+1), (a*2,b), (a,b*2)
@lru_cache(None)
def game(h):
    if sum(h) >= trg:
        return 'w'
    if any(game(m) == 'w' for m in movs(h)):
        return 'p1'
    if all(game(m) == 'p1' for m in movs(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in movs(h)):
        return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in movs(h)):
        return 'B2'
for h in range(1,48):
    num = (5,h)
    if (game(num)) is not None:
        print(game(num),h)# 12, 2123, 20