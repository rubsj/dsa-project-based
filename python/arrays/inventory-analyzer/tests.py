import unittest
from core import (
    has_duplicates,
    most_frequent_product,
    out_of_stock_items,
    reorder_suggestions,
    second_highest_stock,
    stock_summary
)

class TestInventoryAnalyzer(unittest.TestCase):

    def test_has_duplicates(self):
        self.assertTrue(has_duplicates([101, 102, 103, 101]))
        self.assertFalse(has_duplicates([101, 102, 103]))

    def test_most_frequent_product(self):
        self.assertEqual(most_frequent_product([101, 102, 101, 103, 101]), 101)
        self.assertIn(most_frequent_product([101, 102, 102, 103, 103]), [102, 103])
        self.assertIsNone(most_frequent_product([]))

    def test_out_of_stock_items(self):
        self.assertEqual(out_of_stock_items([0, 5, 0], [101, 102, 103]), [101, 103])
        self.assertEqual(out_of_stock_items([1, 2, 3], [101, 102, 103]), [])

    def test_reorder_suggestions(self):
        self.assertEqual(reorder_suggestions([3, 10, 2], [101, 102, 103], 5), [101, 103])
        self.assertEqual(reorder_suggestions([6, 7], [101, 102], 5), [])

    def test_second_highest_stock(self):
        self.assertEqual(second_highest_stock([5, 8, 6], [101, 102, 103]), 103)
        self.assertIsNone(second_highest_stock([5, 5, 5], [101, 102, 103]))
        self.assertIsNone(second_highest_stock([], []))

    def test_stock_summary(self):
        summary = stock_summary([5, 10, 15], [101, 102, 103])
        self.assertEqual(summary["total_products"], 3)
        self.assertEqual(summary["distinct_products"], 3)
        self.assertEqual(summary["average_stock"], 10.0)

if __name__ == '__main__':
    unittest.main()