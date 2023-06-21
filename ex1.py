class Cursor:
    def __init__(
            self,
            type: int = 0,
            x: int = 0,
            y: int = 0,
            size: int = 7) -> None:
        self._x = x
        self._y = y
        self.is_active = True
        if type in [0, 1]:
            self._type = type
        else:
            raise ValueError(
                "Значение типа должно быть либо 0 (горизонтальный), либо 1 (вертикальный)!")
        if size in list(range(1, 16)):
            self._size = size
        else:
            raise ValueError(
                "Значение размера курсора должно быть в диапазоне от 1 до 15!")

    def change_coords(self, x: int = 0, y: int = 0) -> tuple:
        self._x += x
        self._y += y
        return (self._x, self._y)

    def change_type(self) -> int:
        self._type = abs(self._type - 1)
        return self._type

    def change_size(self, size: int = 0) -> int:
        if size in list(range(1, 16)):
            self._size = size
        else:
            raise ValueError(
                "Значение размера курсора должно быть в диапазоне от 1 до 15!")

    def change_active(self) -> bool:
        self.is_active = not self.is_active
        return self.is_active

    def read(self) -> None:
        try:
            self._x = int(input("Введите x: "))
        except ValueError:
            print("Некорректое значение! x = 0")
            self._x = 0

        try:
            self._y = int(input("Введите y: "))
        except ValueError:
            print("Некорректое значение! y = 0")
            self._y = 0

        try:
            self._type = int(
                input("Введите тип (0 - горизонтальный, 1 - вертикальный): "))
        except ValueError:
            print("Некорректое значение!  Тип - горизонтальный")
            self._type = 0

        try:
            size = int(input("Введите размер курсора (1-15): "))
            if size not in list(range(1, 16)):
                raise ValueError
            self._size = size
        except ValueError:
            print("Некорректное значение! Размер курсора - 7")
            self._size = 7

    def display(self) -> dict:
        print(
            f"\nПАРАМЕТРЫ КУРСОРА\n\nКоординаты: [{self._x}, {self._y}]\nСтатус: {'Активен' if self.is_active else 'Погашен'}\nТип: {['Горизонтальный', 'Вертикальный'][self._type]}\nРазмер: {self._size}")
        return {
            "coords": (
                self._x,
                self._y),
            "status": self.is_active,
            "type": self._type,
            "Размер": self._size}


if __name__ == "__main__":
    c = Cursor()
    c.read()
    print(c.display())
    c.change_active()
    c.change_coords(10, 100)
    c.change_size(10)
    c.change_type()
    print(c.display())
