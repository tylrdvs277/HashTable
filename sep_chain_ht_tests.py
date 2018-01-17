# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 8
# Term:        Fall 2017

import unittest
from sep_chain_ht import MyHashTable

class TestLab8(unittest.TestCase):


    def test_insert(self):
        h = MyHashTable()
        h[12] = "dog"
        self.assertEqual(h[12], (12, "dog"))
        self.assertEqual(h.size(), 1)
        h[12] = "cat"
        self.assertEqual(h[12], (12, "cat"))
        self.assertEqual(h.size(), 1)

    def test_get(self):
        h = MyHashTable()
        h[12] = "dog"
        self.assertEqual(h[12], (12, "dog"))
        with self.assertRaises(LookupError):
            h[13]

    def test_remove(self):
        h = MyHashTable()
        h[12] = "dog"
        self.assertEqual(h.remove(12), (12, "dog"))
        self.assertEqual(h.size(), 0)
        with self.assertRaises(LookupError):
            h.remove(13)

    def test_size(self):
        h = MyHashTable()
        for i in range(1, 20):
            h[i] = "random"
            self.assertEqual(i, h.size())

    def test_load_factor(self):
        h = MyHashTable()
        for i in range(1, 10):
            h[i] = "random"
            self.assertEqual(i / 11, h.load_factor())

    def test_collisions(self):
        h = MyHashTable()
        h[1] = "cat"
        self.assertEqual(h.collisions(), 0)
        h[12] = "cat"
        self.assertEqual(h.collisions(), 1)
        h[2] = "cat"
        self.assertEqual(h.collisions(), 1)
        h[23] = "cat"
        self.assertEqual(h.collisions(), 1)
        h[2] = "dog"
        self.assertEqual(h.collisions(), 1)

    def test_grow_table(self):
        h = MyHashTable(5)
        for i in range(7):
            h[i] = "random"
        self.assertEqual(h.load_factor(), 7 / 5)
        h[7] = "random"
        self.assertEqual(h.load_factor(), 8 / 11)


if __name__ == "__main__":
    unittest.main()
