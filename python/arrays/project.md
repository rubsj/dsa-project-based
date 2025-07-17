✅ Mini-Project: Inventory Analyzer (Arrays Module)


🎯 Project Goal
Design a system that analyzes inventory data to detect duplicate products, identify top-selling/reordering items, and calculate stock metrics — using core array manipulation patterns.

📦 Inputs
product_ids = [101, 102, 101, 103, 104, 102, 102, 105]
stock_counts = [5, 2, 7, 0, 3, 1, 4, 6]  # current stock for each ID by index

📤 Outputs (Sample)
{
  "has_duplicates": True,
  "most_frequent_product": 102,
  "out_of_stock_items": [103],
  "reorder_suggestions": [102, 104],  # stock < threshold
  "second_highest_stocked_item": 105,
  "stock_summary": {
    "total_products": 8,
    "distinct_products": 5,
    "average_stock": 3.5
  }
}

💡 Core Features & DSA Patterns

| Feature                     | DSA Pattern/Technique      | Complexity |
| --------------------------- | -------------------------- | ---------- |
| Duplicate Check             | Hashing (`set`)            | O(n)       |
| Most Frequent Product       | Hash Map Frequency Count   | O(n)       |
| Out-of-Stock Detection      | Linear Scan + Condition    | O(n)       |
| Reorder Suggestions         | Filter + Thresholding      | O(n)       |
| Second Highest Stocked Item | Max Tracking (no sort)     | O(n)       |
| Stock Summary (Stats)       | Array Reduction (sum, avg) | O(n)       |

🧱 Basic Functions To Implement
def has_duplicates(product_ids: list[int]) -> bool: ...
def most_frequent_product(product_ids: list[int]) -> int: ...
def out_of_stock_items(stock_counts: list[int], product_ids: list[int]) -> list[int]: ...
def reorder_suggestions(stock_counts: list[int], product_ids: list[int], threshold: int) -> list[int]: ...
def second_highest_stock(stock_counts: list[int], product_ids: list[int]) -> int: ...
def stock_summary(stock_counts: list[int], product_ids: list[int]) -> dict: ...

✅ Core Functions and Their Use Cases
1. has_duplicates(product_ids: list[int]) -> bool
Use Case:
Detects if any product ID has been scanned more than once — helpful to flag potential intake errors or duplicate barcodes.

Example:
```
Input: [101, 102, 103, 101]  
Output: True
```
2. most_frequent_product(product_ids: list[int]) -> int
Use Case:
Identifies the most frequently appearing product ID — useful for analyzing high-volume inventory movement or frequently reordered items.

Example:
```
Input: [101, 102, 101, 103, 101]  
Output: 101
```

3. out_of_stock_items(stock_counts: list[int], product_ids: list[int]) -> list[int]
Use Case:
Returns all product IDs where stock count is 0 — useful for triggering restocking alerts or cleaning up listings.

Example:
```
Input: stock_counts = [0, 5, 2], product_ids = [101, 102, 103]  
Output: [101]
```

4. reorder_suggestions(stock_counts: list[int], product_ids: list[int], threshold: int) -> list[int]
Use Case:
Finds product IDs where stock is below a given threshold — helps generate reorder reports or purchase lists.

Example:

```
Input: stock_counts = [3, 10, 2], threshold = 5  
Output: [101, 103]  # assuming product_ids = [101, 102, 103]
```
5. second_highest_stock(stock_counts: list[int], product_ids: list[int]) -> int
Use Case:
Returns the product ID with the second-highest stock count — useful for analytics or alternate top-seller reports.

Example:

```
Input: stock_counts = [5, 8, 6], product_ids = [101, 102, 103]  
Output: 103
```

6. stock_summary(stock_counts: list[int], product_ids: list[int]) -> dict
Use Case:
Provides an overview of inventory health including:

Total number of items

Number of distinct products

Average stock per product

Example:

```
Output: {
  "total_products": 3,
  "distinct_products": 3,
  "average_stock": 6.3
}
```