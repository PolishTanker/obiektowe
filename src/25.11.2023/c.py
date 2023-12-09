import abc

class Trash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def put_item(self, item, position):
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        if len(self.items) <= position:
            self.items += [None] * (position - len(self.items) + 1)
        self.items[position] = item

    def get_item(self, position):
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        return self.items[position]

    def remove_item(self, position):
        if position < 0 or position >= self.capacity:
            raise ValueError("Invalid position")
        self.items[position] = None

    def size(self):
        return len([item for item in self.items if item is not None])

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.get_item(key)
        raise TypeError("Invalid key type")

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.put_item(value, key)
        raise TypeError("Invalid key type")

    def __delitem__(self, key):
        if isinstance(key, int):
            self.remove_item(key)
        raise TypeError("Invalid key type")