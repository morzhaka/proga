def calc_recursive(i):
    if i == 1 or i == 2:
        return 0
    if i == 3:
        return 1.5
    
    return ((i + 1) / (i*i + 1)) * calc_recursive(i-1) - calc_recursive(i-2) * calc_recursive(i-3)
# Выводим результат

print("v(1) =", calc_recursive(1))
print("v(2) =", calc_recursive(2))
print("v(3) =", calc_recursive(3))
print("v(4) =", calc_recursive(4))
print("v(5) =", calc_recursive(5))
print("v(6) =", calc_recursive(6))
print("v(7) =", calc_recursive(7))
print("v(8) =", calc_recursive(8))
