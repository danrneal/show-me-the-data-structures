"""Create a cache that removes the least recently used when at capacity.

Usage: lru_cache.py

Classes:
    LruCache()
"""


class LruCache:
    """Cache object that removes the least recently used when at capacity.

    Attributes:
        cache: A dict representing the cache object
        call_cache: A dict representing a cache of keys of the most recently
            used resources
        capacity: An int representing the capacity of the cache
        size: An int representing the number of elements currently in the cache
        call_id: An int representing an incrementing number for order of calls
    """

    def __init__(self, capacity):
        """Set-up for a least recently used cache."""
        self.cache = {}
        self.call_cache = {}
        self.capacity = capacity
        self.size = 0
        self.call_id = 0

    def get(self, key):
        """Retrieve a value from the cache.

        Args:
            key: An int representing the key from the cache to retreive

        Returns:
            value: An int representing the value retrieved
        """
        if key not in self.cache:
            return -1

        self.call_cache[self.call_id] = key
        self.call_id += 1

        return self.cache[key]

    def put(self, key, value):
        """Place a value into the cache at the given key.

        Args:
            key: An int representing the key at which to place the value in the
                cache
            value: An int representing the value to place into the cache
        """
        if key not in self.cache:
            if self.size == self.capacity:
                self.remove()
            self.size += 1

        self.cache[key] = value
        self.call_cache[self.call_id] = key
        self.call_id += 1

    def remove(self):
        """Remove the least recently used resource from the cache."""
        call_id = self.call_id - self.capacity
        key = self.call_cache[call_id]
        del self.call_cache[call_id]
        del self.cache[key]


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

    print("All test cases passed!")


if __name__ == "__main__":
    main()
