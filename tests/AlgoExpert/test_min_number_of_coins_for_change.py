import pytest
from src.AlgoExpert.min_number_of_coins_for_change import Solution

# We can define a set of test cases to run against both solutions
# Format: (n, denoms, expected_result)
test_cases = [
    (7, [1, 5, 10], 3),  # 5 + 1 + 1
    (10, [1, 3, 4], 3),  # 4 + 3 + 3 or 3 + 3 + 4, etc.
    (0, [1, 2, 3], 0),   # No change needed
    (3, [2], -1),        # Impossible to make change
    (7, [2, 4], -1),     # Impossible
    (135, [39, 45, 130, 40, 4, 1, 60, 75], 2) # 75 + 60 = 135
]

class TestMinNumberOfCoinsForChange:
    @pytest.mark.parametrize("n, denoms, expected", test_cases)
    def test_solution(self, n, denoms, expected):
        """
        Tests Solution's minNumberOfCoinsForChange method.
        """
        # We pass a copy of denoms to avoid mutating the original list in case it's sorted in-place
        assert Solution.minNumberOfCoinsForChange(n, denoms.copy()) == expected