"""
# 题目 (LeetCode 49. 字母异位词分组 / Group Anagrams)
#
# 给你一个字符串数组 strs ，请你将 字母异位词 (Anagram) 归组一起。
# 字母异位词 是指由字母重新排列后形成的字符串，其所有字母的出现次数相同。
# 返回的结果中每组内部的字母可以任意顺序，但每组内的字符串必须是字母异位词。
#
# 示例 1：
#   输入：strs = ["eat","tea","tan","ate","nat","bat"]
#   输出：[["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 示例 2：
#   输入：strs = [""]
#   输出：[["")]
#
# 示例 3：
#   输入：strs = ["a"]
#   输出：[["a"]]
#
# 提示：
#   1 <= strs.length <= 10^4
#   0 <= strs[i].length <= 100
#   strs[i] 仅包含小写英文字母
#
# 难度：中等
#
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Use an arrays of dicts to check the anagrams
# Approach
<!-- Describe your approach to solving the problem. -->
在 Python 中解决 Group Anagrams 的标准且高效做法是：将排序后的字符串（或字符计数元组）作为 defaultdict(list) 的 Key，将原字符串作为 Value 存入。字母异位词排序后必然得到相同的字符串，因此可用作分组依据。

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n \cdot k \log k)$$，其中 $$n$$ 为字符串数量，$$k$$ 为单个字符串的最大长度。

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n \cdot k)$$，用于存储哈希表。

# Code
```python []

"""
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        
        for s in strs:
            # 将字符串排序后作为 dict 的 key（Anagrams 排序后必然相同）
            key = "".join(sorted(s))
            ans[key].append(s)
            
        return list(ans.values())