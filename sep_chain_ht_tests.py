# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 8
# Term:        Fall 2017

import unittest
import sep_chain_ht

class TestLab8(unittest.TestCase):

    def test_insert(self):
        hash_table = sep_chain_ht.MyHashTable()
        hash_table.insert(12, "dog")
        self.assertEqual(hash_table.get(12), (12, "dog"))
        self.assertEqual(hash_table.size(), 1)
        hash_table.insert(12, "cat")
        self.assertEqual(hash_table.get(12), (12, "cat"))
        self.assertEqual(hash_table.size(), 1)

    def test_get(self):
        hash_table = sep_chain_ht.MyHashTable()
        hash_table.insert(12, "dog")
        self.assertEqual(hash_table.get(12), (12, "dog"))
        with self.assertRaises(LookupError):
            hash_table.get(13)

    def test_remove(self):
        hash_table = sep_chain_ht.MyHashTable()
        hash_table.insert(12, "dog")
        self.assertEqual(hash_table.remove(12), (12, "dog"))
        self.assertEqual(hash_table.size(), 0)
        with self.assertRaises(LookupError):
            hash_table.remove(13)

    def test_size(self):
        hash_table = sep_chain_ht.MyHashTable()
        for i in range(1, 20):
            hash_table.insert(i, "random")
            self.assertEqual(i, hash_table.size())

    def test_load_factor(self):
        hash_table = sep_chain_ht.MyHashTable()
        for i in range(1, 10):
            hash_table.insert(i, "random")
            self.assertEqual(i / 11, hash_table.load_factor())

    def test_collisions(self):
        hash_table = sep_chain_ht.MyHashTable()
        hash_table.insert(1, "cat")
        self.assertEqual(hash_table.collisions(), 0)
        hash_table.insert(12, "cat")
        self.assertEqual(hash_table.collisions(), 1)
        hash_table.insert(2, "cat")
        self.assertEqual(hash_table.collisions(), 1)
        hash_table.insert(23, "cat")
        self.assertEqual(hash_table.collisions(), 1)
        hash_table.insert(2, "dog")
        self.assertEqual(hash_table.collisions(), 1)

    def test_grow_table(self):
        hash_table = sep_chain_ht.MyHashTable(5)
        for i in range(7):
            hash_table.insert(i, "random")
        self.assertEqual(hash_table.load_factor(), 7 / 5)
        hash_table.insert(7, "random")
        self.assertEqual(hash_table.load_factor(), 8 / 11)


if __name__ == "__main__":
    unittest.main()

