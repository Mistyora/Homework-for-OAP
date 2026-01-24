n = int(input())

# Считываем и фильтруем пункты за один раз
recipes = [input() for _ in range(n) if "лук" not in input()]

print(', '.join(recipes))

# или

n = int(input())

# Считываем пункты рецепта и фильтруем те, где нет "лук"
recipes = []
for _ in range(n):
    item = input()
    if "лук" not in item:
        recipes.append(item)

# Выводим результат через запятую и пробел
print(', '.join(recipes))