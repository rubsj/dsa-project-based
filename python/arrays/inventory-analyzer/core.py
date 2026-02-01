from typing import List, Optional, Dict


def has_duplicates(product_ids: List[int]) -> bool:
    """
    Checks if there are any duplicate product IDs in the inventory.
    """
    seen = set()
    for id in product_ids:
        if id in seen:
            return True
        seen.add(id)
    return False


def most_frequent_product(product_ids: List[int]) -> Optional[int]:
    """
    Returns the product ID that appears most frequently.
    If multiple have the same highest frequency, one of them is returned.
    """
    if not product_ids:
        return None

    max_freq = 0
    freq_prodct_id = None
    products_freq = {}
    for id in product_ids:
        freq = products_freq.get(id, 0) + 1
        products_freq[id] = freq
        if freq > max_freq:
            max_freq = freq
            freq_prodct_id = id
    return freq_prodct_id


def out_of_stock_items(stock_counts: List[int], product_ids: List[int]) -> List[int]:
    """
    Returns a list of product IDs that are currently out of stock (stock count = 0).
    """
    return [id for count, id in zip(stock_counts, product_ids) if count == 0]


def reorder_suggestions(
    stock_counts: List[int], product_ids: List[int], threshold: int
) -> List[int]:
    """
    Suggests product IDs that have stock below a specified threshold.
    """
    return [id for count, id in zip(stock_counts, product_ids) if count < threshold]


def second_highest_stock(
    stock_counts: List[int], product_ids: List[int]
) -> Optional[int]:
    """
    Returns the product ID with the second highest stock count.
    If not enough distinct values exist, returns None.
    """
    if not product_ids or len(set(product_ids)) < 2:
        return None
    highest = second_highest = float("-inf")
    highest_id = second_highest_id = None
    for count, id in zip(stock_counts, product_ids):
        if count > highest:
            second_highest, second_highest_id = highest, highest_id
            highest, highest_id = count, id
        elif highest > count > second_highest:
            second_highest, second_highest_id = count, id
    return second_highest_id


def stock_summary(stock_counts: List[int], product_ids: List[int]) -> Dict[str, float]:
    """
    Returns a dictionary summary of stock metrics.
    Provides an overview of inventory health including:
        Total number of items
        Number of distinct products
        Average stock per product
    """
    total_products = len(stock_counts)
    distinct_products = len(set(product_ids))
    average_stock = sum(stock_counts) / total_products if total_products > 0 else 0.0
    return {
        "total_products": total_products,
        "distinct_products": distinct_products,
        "average_stock": average_stock,
    }


def aggregate_stock_by_product(
    product_ids: List[int], stock_counts: List[int]
) -> Dict[int, int]:
    """
    Aggregate total stock for each distinct product ID
    Input:
        product_ids = [101, 102, 101, 103]
        stock_counts = [5, 2, 7, 3]

    Output:
        {101: 12, 102: 2, 103: 3}

    """
    aggregate = {}
    for id, stock in zip(product_ids, stock_counts):
        if id in aggregate:
            aggregate[id] = aggregate[id] + stock
        else:
            aggregate[id] = stock
    return aggregate


def has_stock_spike_window(
    stock_counts: List[int], window_size: int, threshold: int
) -> bool:
    """
    Detect if any 3-day sliding window has total stock exceeding a threshold.
    stock_counts = [1, 3, 7, 4, 2]
        threshold = 12
        Output: True (because 7+4+2 = 13)
    """
    if len(stock_counts) < window_size:
        return False
    
    slideVal = sum(stock_counts[0: window_size])
    # Check the first window
    if slideVal > threshold:
        return True
    
    for i, stock in enumerate(stock_counts, start=window_size):
        slideVal = slideVal - stock_counts[i - window_size] + stock
        if slideVal > threshold:
            return True
    return False


def longest_mountain_stock_run(stock_counts: List[int]) -> int:
    """
    Find the length of the longest subarray where stock is increasing then decreasing (like a mountain).
        stock_counts = [1, 2, 3, 2, 1, 2, 3, 4]
        Output: 5  (subarray: [1,2,3,2,1])
    """

    left = right = 0
    longest = 0
    n = len(stock_counts)
    i = 1
    while i < n - 1:
        if stock_counts[i - 1] < stock_counts[i] > stock_counts[i + 1]:
            left = i - 1
            right = i + 1
            while left > 0 and stock_counts[left - 1] < stock_counts[left]:
                left = left - 1
            while right < n - 1 and stock_counts[right + 1] < stock_counts[right]:
                right = right + 1
            longest = max(longest, right - left + 1)
            i = right
        else:
            i = i + 1

    return longest
