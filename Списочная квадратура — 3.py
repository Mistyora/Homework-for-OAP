numbers = input().split()

# Преобразуем строки в числа и возводим в квадрат
squares = [str(int(num)**2) for num in numbers]

# Объединяем квадраты в строку через пробел
print(' '.join(squares))