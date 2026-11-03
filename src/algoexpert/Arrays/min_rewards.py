def minRewards(scores):
    """
    Calculate the minimum total rewards to distribute to students such that:
    - Each student receives at least one reward.
    - Students with higher scores than their immediate neighbors receive more rewards than those neighbors.
    
    Time Complexity: O(n) - two linear passes through the scores array
    Space Complexity: O(n) - rewards array of size n
    
    Examples:
    >>> minRewards([8, 4, 2, 1])
    8
    >>> minRewards([1, 2, 2])
    4
    """
    if not scores:
        return 0

    n = len(scores)
    rewards = [1] * n

    # 第一遍：从左向右扫描，确保右边分数高于左边时，奖励递增
    for i in range(1, n):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    # 第二遍：从右向左扫描，确保左边分数高于右边时，奖励满足条件
    for i in range(n - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    return sum(rewards)