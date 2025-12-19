def func(*son):
    s = sum(son)
    return s // len(son)
print(func(1,2,3))