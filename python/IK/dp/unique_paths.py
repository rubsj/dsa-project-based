
def unique_paths(n, m):
    """
    Args:
     n(int32)
     m(int32)
    Returns:
     int32
    """
    # Interpret parameters as `n` rows and `m` columns.
    # Use a DP table of size `n x m` where dp[r][c]
    # is the number of unique paths to reach cell (r,c).
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("n and m must be integers")
    if n <= 0 or m <= 0:
        return 0

    dp = [[0] * m for _ in range(n)]
    for row in range(n):
        dp[row][0] = 1
        
    for col in range(m):
        dp[0][col] = 1
        
    for row in range(1, n):
        for col in range(1, m):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[n-1][m-1]


if __name__ == "__main__":
    import unittest

    class TestUniquePaths(unittest.TestCase):
        def test_example_cases(self):
            self.assertEqual(unique_paths(3, 2), 3)
            self.assertEqual(unique_paths(3, 3), 6)

        def test_edge_cases(self):
            self.assertEqual(unique_paths(1, 1), 1)
            self.assertEqual(unique_paths(0, 5), 0)
            self.assertEqual(unique_paths(5, 0), 0)

        def test_small_cases(self):
            self.assertEqual(unique_paths(2, 2), 2)
            self.assertEqual(unique_paths(2, 3), 3)

    unittest.main()

result = unique_paths(3, 2)
print(result)  # Expected output: 3