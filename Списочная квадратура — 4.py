# print(*[x**2 for x in map(int, input().split()) if x % 2 != 0 and str(x**2)[-1] != '9'])

print(' '.join([str(int(x)**2) for x in input().split() if int(x) % 2 == 1 and str(int(x)**2)[-1] != '9']))

# Считываем входную строку и разбиваем на список строк по пробелам
input_numbers = input().split()

# Создаём пустой список для результатов
result = []

# Перебираем каждое число из входного списка
for x in input_numbers:
    # Преобразуем строку в целое число
    num = int(x)

    # Проверяем, что число нечётное
    if num % 2 == 1:
        # Возводим в квадрат
        square = num ** 2

        # Проверяем, что последняя цифра квадрата не '9'
        if str(square)[-1] != '9':
            # Добавляем квадрат в результат (в виде строки)
            result.append(str(square))

# Объединяем все элементы списка через пробел и выводим
print(' '.join(result))



