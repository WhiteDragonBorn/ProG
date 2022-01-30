#1921 --- P01 --- KP



from functools import lru_cache
trg = 29
def moves(h):
    return h+1,h*2
@lru_cache(None)
def game(h):
    if h >= trg:
        return 'w'
    if any(game(m) == 'w' for m in moves(h)):
        return 'p1'
    if all(game(m) == 'p1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'p2'
    if all(game(m) == 'p2'or game(m)== 'p1' for m in moves(h)):
        return 'B2' 
for h in range(1,29):
    if game(h) is not None:
        print(game(h),h) # 14, 7 13, 12