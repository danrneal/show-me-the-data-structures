"""Create a cache that removes the least recently used when at capacity.

Usage: lru_cache.py

Classes:
    LruCache()
"""


class LruCache:
    """Cache object that removes the least recently used when at capacity.

    Attributes:
        cache: A dict representing the cache object holding nodes to a double
            linked list holding LruCacheNode objects
        capacity: An int representing the capacity of the cache
        head: A LruCacheNode representing the most recently used object in the
            cache and the beginning of a doubly linked list
        tail: A LruCacheNode representing the least recently used object in the
            cache and the beginning of a doubly linked list
    """

    def __init__(self, capacity):
        """Set-up for a least recently used cache."""
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key):
        """Retrieve a value from the cache.

        Args:
            key: An int representing the key from the cache to retreive

        Returns:
            value: An int representing the value retrieved
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.update_most_recently_used(node)

        return node.value

    def put(self, key, value):
        """Place a value into the cache at the given key.

        Args:
            key: An int representing the key at which to place the value in the
                cache
            value: An int representing the value to place into the cache
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_most_recently_used(node)
            return

        if len(self.cache) == self.capacity:
            self.remove()

        node = LruCacheNode(key, value, self.head)
        self.cache[key] = node
        self.head = node

        if node.next is None:
            self.tail = node
        else:
            node.next.prev = node

    def remove(self):
        """Remove the least recently used resource from the cache."""
        del self.cache[self.tail.key]
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
            return

        self.tail.next.prev = None
        self.tail.next = None

    def update_most_recently_used(self, node):
        """Move a node to the head of the doubly linked list.

        Args:
            node: A LruCacheNode representing the most recently used
        """
        if node == self.head:
            return

        if node == self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        node.prev.next = node.next
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node


class LruCacheNode:
    """Creates a Node object for a Least Recently Used Cache.

    Attributes:
        key: An int representing the key the node is stored at in the cache
        value: An int representing the value to store in the cache
        prev: A LruCache Node object representing the previous node in a doubly
            linked list
        next: A LruCache Node object representing the next node in a doubly
            linked list
    """

    def __init__(self, key, value, head):
        """Set-up for a least recently used cache node."""
        self.key = key
        self.value = value
        self.prev = None
        self.next = head


def main():
    """Main function call to test the functionality of the LruCache."""
    our_cache = LruCache(5)
    our_cache.put(1, 1)
    our_cache.put(2, 2)
    our_cache.put(3, 3)
    our_cache.put(4, 4)
    assert our_cache.get(1) == 1
    assert our_cache.get(2) == 2
    assert our_cache.get(9) == -1
    our_cache.put(5, 5)
    our_cache.put(6, 6)
    assert our_cache.get(3) == -1

    our_cache = LruCache(3)
    our_cache.put(1, 1)
    our_cache.put(2, 2)
    our_cache.put(3, 3)
    our_cache.put(4, 4)
    assert our_cache.get(4) == 4
    assert our_cache.get(1) == -1
    our_cache.put(2, 4)
    assert our_cache.get(2) == 4
    our_cache.put(5, 5)
    assert our_cache.get(3) == -1

    print("All test cases passed!")


if __name__ == "__main__":
    main()
