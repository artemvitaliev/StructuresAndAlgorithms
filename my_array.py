from typing import Any, Callable

class MyArray:
    def __init__(self, length: int, array: list = None, default_value = 0):
        if length > 0:
            self._length = length
        else:
            raise ValueError("Length must be positive and greater than 0")

        if array is None:
            self._array = [default_value] * length
        elif len(array) < self._length:
            self._array = array + [default_value] * (self._length - len(array))
        elif len(array) > self._length:
            raise ValueError("Array length exceeds specified length")
        else:
            self._array = array.copy()

    def __repr__(self):
        return f"MyArray({self._array})"

    def __str__(self):
        return str(self._array)

    def __len__(self):
        return self._length

    def __abs__(self):
        return MyArray(self._length, list(map(abs, self._array)))

    def __getitem__(self, key):
        return self._array[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        elif key >= self._length or key < -self._length:
            raise IndexError("Index out of range")
        else:
            self._array[key] = value

    def sort(self, key = None, reverse = False):
        return MyArray(self._length, sorted(self._array, key=key, reverse=reverse))

    def find(self, predicate: Callable[[Any], bool], start: int = 0, end: int = None):
        if end is None:
            end = self._length

        try:
            start, end, _ = slice(start, end).indices(self._length)
        except ValueError:
            return -1

        for i in range(start, end):
            if predicate(self._array[i]):
                return i

        return -1