class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.length = 0
        self.hash_table = [(None, None) for _ in range(self.size)]

    def resize(self):
        self.size *= 2
        self.hash_table.extend([(None, None)] * self.size)
        for old_key, old_value in self.hash_table:
            if old_key:
                self.hash_table[hash(old_key) % self.size] = (old_key, old_value)

    def __setitem__(self, key, value):
        if self.length * 2 > self.size:
            self.resize()
        if self.hash_table[hash(key) % self.size][0] != key:
            self.length += 1
        self.hash_table[hash(key) % self.size] = (key, value)

    def __getitem__(self, item):
        if self.hash_table[hash(item) % self.size][0] != item:
            raise KeyError
        return self.hash_table[hash(item) % self.size][1]

    def __len__(self) -> int:
        return self.length


if __name__ == "__main__":
    t = HashTable()
    t["a"] = 1
    t["b"] = 2
    t["c"] = "first_value"
    print(t["c"])
    print(len(t))
    t["c"] = "second_value"
    print(t["c"])
    print(len(t))
