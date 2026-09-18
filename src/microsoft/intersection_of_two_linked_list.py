"""
Intersection of Two Linked Lists (LeetCode 160)

Given the heads of two singly linked-lists headA and headB, return the node where
the intersection begins. If the two linked lists have no intersection at all, return null.

The linked lists are 1-indexed or 0-indexed? They are not (standard):
- The inputs are the heads of two independent lists.
- There are no cycles in either list.
- The intersection (if any) is defined by reference, not value.

Example:
    Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    (skipA / skipB describe how many nodes to skip in each list before the shared tail)
    Output: the node with value 8 (the reference-intersection node)

    Explanation:
        listA: 4 -> 1 -> 8 -> 4 -> 5
        listB: 5 -> 6 -> 1 -> 8 -> 4 -> 5
        The red (shared) portion starts at the node with value 8.

If the two lists have no intersection, return null.

Intuition:
A set can be used to record every node already visited while traversing a list.
To iterate / traverse a set in Python you simply walk the collection, e.g.
`for node in iterated:` or, while scanning a list, test membership with
`if node in iterated:`. Each ListNode is hashable by object identity, so the set
stores references and membership tests detect the *same* node object appearing in
both lists. As soon as a node already inside the set is met again, that node is the
intersection; if both lists are exhausted without a repeat, there is no intersection.

Two-pointer technique (O(1) space): let pA walk headA then switch to headB, and
pB walk headB then switch to headA. Because the two pointers traverse the same
combined length (|A| + |B|), they are guaranteed to meet at the intersection node
(or both fall off the end as null) in a single synchronized pass.

Time: O(m + n), Space: O(m + n) for the set approach / O(1) for the two-pointer approach
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionViaSet(self, headA, headB):
        """
        Find the intersection node using a set to remember visited nodes.

        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode

        Iterating / traversing a set:
            - Membership test:  `if node in iterated:`  -> O(1) average
            - Walk the whole set: `for node in iterated:` -> iterates in arbitrary order
            - Each ListNode is hashable by identity (id), so the set stores object
              references. Two lists sharing a node share the *same* object, which the
              set detects on the second encounter.
        """
        iterated = set()
        a = headA
        b = headB
        while a or b:
            if a is not None:
                if a in iterated:
                    return a
                else:
                    iterated.add(a)
                    a = a.next
            if b is not None:
                if b in iterated:
                    return b
                else:
                    iterated.add(b)
                    b = b.next

        return None

    def getIntersectionFullTwoListLength(self, headA, headB):
        """
        Find the intersection node using the two-pointer technique (O(1) space).

        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode

        Algorithm:
            Let pA start at headA and pB start at headB. Each pointer walks its own
            list; when it reaches the end of its list it is *re-routed* to the other
            list's head. Because both pointers traverse the combined length
            (|A| + |B|), they stay in lock-step after swapping and are guaranteed to
            meet at the intersection node (or both land on None simultaneously if
            there is no intersection).

            Why it works:
                - If the two lists have equal length, the pointers meet within the
                  first pass.
                - If lengths differ by |lenA - lenB|, the longer-list pointer absorbs
                  that offset, then both pointers advance together from the same
                  position on the shared tail.
                - After at most two full traversals each, pA == pB: either at the
                  intersection node or at None.

        Time: O(m + n), Space: O(1)
        """
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA

    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        return self.getIntersectionFullTwoListLength(headA, headB)
