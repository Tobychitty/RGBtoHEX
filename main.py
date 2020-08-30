r = int(input("Input R value: "))
g = int(input("Input G value: "))
b = int(input("Input B value: "))


def rgb(r, g, b):
    print('#{0:02x}{1:02x}{2:02x}'.format(range_check(r), range_check(g), range_check(b)).upper())


def range_check(x):
    return max(0, min(x, 255))


rgb(r, g, b)
