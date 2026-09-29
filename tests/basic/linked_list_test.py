from unittest import TestCase

from basic.linked_list import LinkedList


class LinkedListTest(TestCase):
    def setUp(self):
        self.l = LinkedList()
        self.l.add(5).add(8).add(12)  # root -> 12 -> 8 -> 5 -> None

    def test_add_and_size(self):
        self.assertEqual(self.l.size, 3)
        # root is the most recently added node (12)
        self.assertEqual(self.l.root.val, 12)

    def test_find(self):
        found = self.l.find(8)
        self.assertIsNotNone(found)
        self.assertEqual(found.val, 8)
        # missing value
        self.assertIsNone(self.l.find(99))

    def test_remove(self):
        self.assertTrue(self.l.remove(8))
        self.assertEqual(self.l.size, 2)
        self.assertIsNone(self.l.find(8))
        # remove the root
        self.assertTrue(self.l.remove(12))
        self.assertEqual(self.l.size, 1)
        self.assertEqual(self.l.root.val, 5)
        # remove from an empty list is a no-op
        l2 = LinkedList()
        self.assertFalse(l2.remove(1))

    def test_remove_last_remaining_node(self):
        self.assertTrue(self.l.remove(12))
        self.assertTrue(self.l.remove(8))
        self.assertTrue(self.l.remove(5))
        self.assertEqual(self.l.size, 0)
        self.assertIsNone(self.l.root)
