import numpy
import random

def print_matrix(m):
    for row in m:
        for col in row:
            print(col, end=' ')
        print()

def out_data(m):
    # Работаем в рамках контекста файла
    with open("out_2.txt", "a+") as f:    # Открываем файл и присваиваем его переменной
        for row in m:
            for col in row:
                f.write(f"{col} ")       # Записываем строку в файл
            f.write("\n")
        f.write("\n")


if __name__ == "__main__":
    n = random.randint(3, 5)
    m = random.randint(3, 5)
    l = random.randint(3, 5)

    # Генерация матрицы NxM с числами в диапазоне от 1 до 10
    a = numpy.random.randint(1, 10, (n, m))

    print(f"Строки: {n}")
    print(f"Столбцы: {m}")
    l_row = list(a[random.randint(0, n-1)])
    print(f"L-строка: {l_row}\n")

    print("Матрица до:")
    print_matrix(a)

    out_data(a)

    # Суммирование элементов L-строки и строки матрицы 
    for row in a:
        row += l_row

    out_data(a)
 
    print("\nМатрица после:")
    print_matrix(a)
