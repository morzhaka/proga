import math

def calc_geom(shape, a, b=None, c=None):
    if shape == "Шар":
        return 4/3 * math.pi * a**3, 4 * math.pi * a**2
    if shape == "Тетраэдр":
        return (a**3)/(6*math.sqrt(2)), (a**2)*math.sqrt(3)
    if shape == "Параллелепипед":
        # если b и c не указаны, считаем куб
        if b is None:
            b = a
        if c is None:
            c = a
        return a * b * c, 2*(a*b + a*c + b*c)
    return 0, 0