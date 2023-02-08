ALPHABET = "qwertyuiopasdfghjklzxcvbnm1234567890_"


class Row():
    idx = 0

    def __init__(self, idx: int):
        self.idx = idx

    def get_idx(self):
        return self.idx

    def set_idx(self, val):
        self.idx = val


class RowModel(Row):
    idx = 0
    nickname = ""
    text = ""
    likes = 0

    def __init__(self, idx: int, nickname: str, text: str, likes: int):
        super().__init__(idx)
        self.nickname = nickname
        self.text = text
        self.likes = likes

    def __str__(self):
        return f"Запись №{self.idx}\nОт кого: {self.nickname}\nЛайки: {self.likes}\nТекст: {self.text}\n"

    def __repr__(self):
        return f"RowModel(idx={self.idx},nickname={self.nickname},text={self.text},likes={self.likes})"

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value


class Data():
    file_path = ""
    data = []
    pointer = 0

    def __init__(self, path: str):
        self.file_path = path
        self.data = self.parse(self.file_path)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f"Контейнер хранит в себе следующее:\n{d_str}"

    def __repr__(self):
        return f"Data({[repr(rm) for rm in self.data]})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.data):
            self.pointer = 0
            raise StopIteration
        else:
            self.pointer += 1
            return self.data[self.pointer-1]

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом.")
 
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс.")

    def as_generator(self):
        self.pointer = 0

        while self.pointer < len(self.data):
            yield self.data[self.pointer]
            self.pointer += 1

    def sorted_by_nickname(self) -> list:
        return sorted(self.data, key=lambda f: f.nickname)

    def sorted_by_likes_count(self) -> list:
        return sorted(self.data, key=lambda f: f.likes, reverse=True)

    def select_rows_with_likes_count_more_than(self, value) -> list:
        return [rm for rm in self.data if rm.likes > value]

    def add_new(self, nickname, text):
        self.data.append(RowModel(len(self.data)+1, nickname, text,0))
        self.save(self.file_path, self.data)

    @staticmethod
    def parse(path: str) -> list:
        parsed = []

        with open(path, "r") as raw_csv:
            for line in raw_csv:
                (idx, nick, text, likes) = line.replace("\n", "").split(",")
                parsed.append(RowModel(int(idx), nick, text, int(likes)))

        return parsed

    @staticmethod
    def save(path, new_data):
        with open(path, "w") as f:
            for rm in new_data:
                f.write(f"{rm.idx},{rm.nickname},{rm.text},{rm.likes}\n")


if __name__ == "__main__":
    d = Data("data_3.csv")

    print("Используем итератор:\n")

    for item in iter(d):
        print(item)

    print("-"*64)

    print("Используем генератор:\n")

    for item in d.as_generator():
        print(item)

    print("="*64)

    print("Сортировка по никнейму:\n")

    for item in d.sorted_by_nickname():
        print(item)

    print("-"*64)

    print("Сортировка по количеству лайков:\n")

    for item in d.sorted_by_likes_count():
        print(item)

    print("-"*64)

    print("Выборка постов, где количество лайков больше 500:\n")

    for item in d.select_rows_with_likes_count_more_than(500):
        print(item)

    print("="*64)

    print("Добавление данных:")
    d.add_new(input("Никнейм: "), input("Текст: "))
    print()
    
    for item in iter(d):
        print(item)

    print("="*64)

    print("Выборка по индексу:")
    idx = int(input("Индекс: "))
    print(f"\n{d[idx]}")
