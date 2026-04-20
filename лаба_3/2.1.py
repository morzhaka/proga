def calc_iterative(k):
    if k == 1 or k == 2:
        return 0
    if k == 3:
        return 1.5
    
    a, b, c = 0, 0, 1.5  # v1, v2, v3
    
    for i in range(4, k + 1):
        d = ((i + 1) / (i*i + 1)) * c - b * a  
        a, b, c = b, c, d
    
    return c

# Выводим результат
print("v(1) =", calc_iterative(1))
print("v(2) =", calc_iterative(2))
print("v(3) =", calc_iterative(3))
print("v(4) =", calc_iterative(4))
print("v(5) =", calc_iterative(5))
print("v(6) =", calc_iterative(6))
print("v(7) =", calc_iterative(7))
print("v(8) =", calc_iterative(8))