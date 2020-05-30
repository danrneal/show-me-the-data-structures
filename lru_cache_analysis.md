# LRU Cache

## Design Choices

I implemented the cache as a dictionary where its keys point to nodes of a doubly linked list so that the nodes could be retrieved in constant time. The doubly linked list also allows for the retrieved node to be be moved in the list in constant time in order to keep track of which node was the least recently used and thus subject to removal when the list reaches capacity.

## Time Complexity

The get, put, and remove functions all operate in O(1) time.

## Space Complexity

The cache operates with a space complexity of O(n) until the cache reaches capacity at which point the size of the cache no longer grows and stays constant with a space complexity of O(1).
