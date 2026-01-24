n = int(input())

# Создаём список квадратов с помощью списочного выражения
squares = [str(i**2) for i in range(n)]

# Выводим результат, используя join
print(' '.join(squares))