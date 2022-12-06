from copy import copy


class matrix:
    def __init__(self, lists: list):
        self.lists = lists
        self.length_matrix_y = len(lists)
        self.length_matrix_x = len(lists[0])
        self.index_x = 0
        self.index_y = 0

    def __iter__(self):
        return self

    def __next__(self):
        value_x = copy(self.index_x)
        value_y = copy(self.index_y)

        if self.index_x < self.length_matrix_x:
            self.index_x += 1
        else:
            value_x = 0
            value_y += 1
            self.index_x = 1
            self.index_y += 1

            if self.index_y == self.length_matrix_y:
                raise StopIteration

        return self.lists[value_y][value_x]
