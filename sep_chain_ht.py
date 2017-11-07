# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 8
# Term:        Fall 2017

class MyHashTable:

    def __init__(self, table_size = 11):
        self.table = [[] for _ in range(table_size)]
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key, item):
        self.num_items += 1
        if self.load_factor() > 1.5:
            self.grow_table()
        table_idx = key % len(self.table)
        for entry_idx in range(len(self.table[table_idx])):
            self.num_collisions += 1
            if self.table[table_idx][entry_idx][0] == key:
                self.table[table_idx][entry_idx] = (key, item)
                return
        self.table[table_idx].append((key, item))

    def grow_table(self):
        new_table = [[] for _ in range(2 * len(self.table) + 1)]
        for slot in self.table:
            for entry in slot:
                new_table[entry[0] % len(new_table)].append(entry)
        self.table = new_table

    def get(self, key):
        slot_idx = key % len(self.table)
        for entry in self.table[slot_idx]:
            if entry[0] == key:
                return entry
        raise LookupError

    def remove(self, key):
        slot_idx = key % len(self.table)
        for entry in self.table[slot_idx]:
            if entry[0] == key:
                self.table[slot_idx].remove(entry)
                self.num_items -= 1
                return entry
        raise LookupError

    def size(self):
        return self.num_items

    def load_factor(self):
        return self.size() / len(self.table)

    def collisions(self):
        return self.num_collisions

    def __setitem__(self, key, item):
        self.insert(key, item)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except LookupError:
            return False

    def __iter__(self):
        for slot in self.table:
            for entry in slot:
                yield entry
