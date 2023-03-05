import random

ARRAY_LIN = [random.randint(1, 1000) for _ in range(10)]
ARRAY_SORTED = [random.randint(1, 1000) for _ in range(10)]


# O(n)
def linear_search():
    print(*ARRAY_LIN)

    curr_min = ARRAY_LIN[0]

    for val in ARRAY_LIN:
        if val < curr_min:
            curr_min = val

    return curr_min


# O(1) (если не учитывать время сортировки (или на вход пришел сразу отсортированный массив))
def first_pick():
    print(*ARRAY_SORTED)

    return sorted(ARRAY_SORTED)[0]


if __name__ == "__main__":
    print(linear_search(), end="\n\n")
    print(first_pick())
