"""
LRU Cache implementation using a doubly linked list + hash map.

Design:
1. `Item` holds key, val, prev, next pointers.
2. `self.cache` is a dict mapping key -> Item for O(1) lookup.
3. A doubly linked list is maintained where:
   - `self.head` is the most recently used item (front).
   - `self.tail` is the least recently used item (back).
4. On get/put of an existing key, move that item to the head.
5. On put of a new key when at capacity, evict the tail.
"""


class Item:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: "Item | None" = None
        self.next: "Item | None" = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Item] = {}
        # Sentinel nodes simplify edge cases (head/tail never None).
        self.head = Item(0, 0)
        self.tail = Item(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, item: Item) -> None:
        """Remove an item from the doubly linked list."""
        prev, nxt = item.prev, item.next
        if prev is not None:
            prev.next = nxt
        if nxt is not None:
            nxt.prev = prev
        item.prev = None
        item.next = None

    def _add_to_head(self, item: Item) -> None:
        """Insert an item right after the head sentinel (most recently used)."""
        item.prev = self.head
        item.next = self.head.next
        if self.head.next is not None:
            self.head.next.prev = item
        self.head.next = item

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        item = self.cache[key]
        self._remove(item)
        self._add_to_head(item)
        return item.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            item = self.cache[key]
            item.val = value
            self._remove(item)
            self._add_to_head(item)
            return

        # Evict if at capacity BEFORE inserting the new item.
        if len(self.cache) >= self.capacity:
            lru = self.tail.prev
            if lru is not None and lru is not self.head:
                self._remove(lru)
                del self.cache[lru.key]

        new_item = Item(key, value)
        self.cache[key] = new_item
        self._add_to_head(new_item)


if __name__ == "__main__":
    actions = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
    key_values = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    capacity = 2
    obj = LRUCache(capacity)

    expected = [None, None, 1, None, -1, None, -1, 3, 4]

    for i, action in enumerate(actions):
        if action == "put":
            obj.put(key_values[i][0], key_values[i][1])
            print(f"put({key_values[i][0]}, {key_values[i][1]}) -> expected {expected[i]}")
        elif action == "get":
            got = obj.get(key_values[i][0])
            ok = "OK" if got == expected[i] else "FAIL"
            print(f"get({key_values[i][0]}) = {got} (expected {expected[i]}) [{ok}]")