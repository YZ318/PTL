def find_numbers(S, P):
    for x in range(1, 1001):
        for y in range(1, 1001):
            if x + y == S and x * y == P:
                return x, y
    return None


S = 10
P = 24
numbers = find_numbers(S, P)
if numbers:
    print("Задуманные числа Петей:", numbers)
else:
    print("Невозможно найти числа, удовлетворяющие условию")
