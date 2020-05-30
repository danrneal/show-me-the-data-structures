# Union and Intersection

## Design Choices

I added a method called contains to the linked list class so that I would be able to not add duplicates to the final sets.

## Time Complexity

The contains method will look up the value in a dict that stores each element so the lookup will have time complexity of O(n).

Finding the union and intersection will go through each linked list once which will be O(n+m)) for both functions.

## Space Complexity

Both union and intersection functions create a new linked list to return. The worst case is that all elements in both input linked lists end up in the final linked list which makes the space complexity O(n+m) for both functions.
