# Union and Intersection

## Design Choices

I used a set to store what values were already contained in the linked list so that I could avoid adding duplicates to the final sets.

## Time Complexity

The set containing the values currently in the linked list will look up the value in a set so the lookup will have time complexity of O(n).

Finding the union and intersection will go through each linked list once which will be O(n+m)) for both functions.

## Space Complexity

Both union and intersection functions create a new linked list to return. The worst case is that all elements in both input linked lists end up in the final linked list which makes the space complexity O(n+m) for both functions.
