def func(a, b, c):
    print(a, b, c)


# func(1, 2, 3)


def func(a, *, b, c):
    print(a, b, c)


func(1, b=2, c=3)
