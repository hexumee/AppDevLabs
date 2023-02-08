import random

NO_STDLIB = True
USES_RANDOM = False

# Нахождение индекса максимального элемента
def find_max_index(a):
    max_idx = None    # Начальный максимальный индекс
    max_val = a[0]    # Начальный максимальное значение

    for (idx, val) in enumerate(a):
        if val > max_val:
            max_val = val
            max_idx = idx

    return max_idx


if __name__ == "__main__":
    if USES_RANDOM:
        # Генерация и вывод 10 чисел
        a = [random.randint(1, 100) for _ in range(10)]
        print(*a)
    else:
        # Получение чисел в виде строки и преобразование в список
        # Также здесь есть проверка на правильность ввода
        try:
            a = list(map(int, input("Введите числа: ").split()))
        except ValueError:
            print("Введены неверные данные.")
            exit()

    if NO_STDLIB:
        a_max_index = find_max_index(a)
    else:
        # Ищем сначала максимальный элемент, а потом его индекс (первое вхождение)
        a_max_index = a.index(max(a))

    offset = 0    # Количество удалений (сдвиг удаления)
    for i in range(a_max_index+1, len(a)):
        if a[i-offset] % 2 == 0:
            a.remove(a[i-offset])
            offset += 1

    print(*a)
