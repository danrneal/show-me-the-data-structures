# Union and Intersection

## Design Choices

I added a method called contains to the linked list class so that I would be able to not add duplicates to the final sets.

## Time Complexity

The method contains will go through each element once in the worst case making its time complexity O(n).

Finding the union will go through each linked list once which will be O(n+m) while then using the contains method on the returned linked list each iteration with inputs of 1...n+m which will be O(log(n+m)). Taking both of those together the complexity of union will be o((n+m)log(n+m)).

Finding the intersection will go through the first linked list which will be O(n) while then using the contains method each iteration on both the second linked list and the final linked list which will have O(m) and O(log(n+m)) respectively. Taking all parts together the intersection function will have time complexity of O(nm\*log(n+m)).

## Space Complexity

Both union and intersection functions create a new linked list to return. The worst case is that all elements in both input linked lists end up in the final linked list which makes the space complexity O(n+m) for both functions.
