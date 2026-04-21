from functools import reduce

def prime_generator(limit):
    for num in range(2, limit + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

def add(x, y):
    return x + y

# Теперь функция выглядит максимально изящно и профессионально:
def sum_primes(limit):
    # Мы передаем генератор напрямую в reduce, без создания списка
    return reduce(add, prime_generator(limit), 0)

print(sum_primes(20))  # 77
print(sum_primes(50))  # 328