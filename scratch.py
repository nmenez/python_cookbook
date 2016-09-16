def yield_play():
    x= 0
    while x < 20:
        yield x
        x += 1


blar = yield_play()
print(blar.__class__)
print(dir(blar))
print(next(blar))
print(next(blar))