# Лабораторна робота №6

# ★ Завдання 2. Прості числа 

N = int(input("Введіть число N: "))

print(f"Прості числа від 2 до {N}:")

number = 2

while number <= N:
    is_prime = True
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(number)

    number += 1
