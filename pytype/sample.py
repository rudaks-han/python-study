# def unannotated(x, y):
#     return " + ".join(x, y)


# unannotated("1", "2")


def annotated(x: int, y: int) -> int:
    return x + y


print(annotated(1, "2"))
