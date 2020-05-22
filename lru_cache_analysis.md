# LRU Cache

## Design Choices

I implemented the cache as a dictionary so that values could be retrieved in constant time. I also implemented another dictionary that kept track of the calls that were the most recently used. This allowed me to lookup the least recently used key when it comes time for removal. Lastly in order to keep track of the order of the most recent calls I gave each call an incrementing id.

## Time Complexity

The get, put, and remove functions all operate in O(1) time.

## Space Complexity

The cache and call_cache both operate with a space complexity of O(n) until the cache reaches capacity at which point the size of the cache no longer grows and stays constant with a space complexity of O(1).
