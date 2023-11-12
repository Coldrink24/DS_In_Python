import ctypes


class MyArray:
    # [1] constructor [2] getters & setters [3] iterator  [4] Size
    # [5] clear [6] data: index - elements - size

    # Constructor
    def __init__(self, size):
        assert size > 0, 'Size can not be zero.'
        self.size = size
        self._next_item = -1

        array = ctypes.py_object * size
        self._elements = array()

    # Actuators & Mutators
    # Makes our array subscriptable
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), 'Array subscript out of range'
        return self._elements[index]

    # Makes our array subscriptable
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), 'Array subscript out of range'
        self._elements[index] = value

    # Iterator
    def __iter__(self):
        return self

    def __next__(self):
        if self._next_item < len(self) - 1:
            self._next_item += 1
            return self._elements[self._next_item]
        else:
            raise StopIteration

    # Size
    def __len__(self):
        return self.size

    # Clear
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value