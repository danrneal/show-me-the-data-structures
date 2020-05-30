"""Take the union and/or intersection of two linked lists.

Usage: union_and_intersection.py

Classes:
    LinkedList()
    Node()
"""


class LinkedList:
    """A linked list where each node points to the next node.

    Attributes:
        head: A Node object that represents the first node in the linked list
    """

    def __init__(self):
        """Set-up for the linked list."""
        self.head = None
        self.nodes = {}

    def __repr__(self):
        """Represents the linked list node values as regular python list."""
        linked_list = []

        node = self.head
        while node is not None:
            linked_list.append(node.value)
            node = node.next

        return str(linked_list)

    def push(self, value):
        """Add a node to the head of the list.

        Args:
            value: The value of the node to insert
        """
        node = Node(value)
        self.nodes[value] = node

        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def contains(self, value):
        """Determine whether a node exists in the linked list or not.

        Args:
            value: The value to search for in the linked list

        Returns:
            A bool representing whether the value was found in an node in the
                linked list
        """
        return value in self.nodes


class Node:
    """A node to store in a linked list.

    Attributes:
        value: The value to store in the node
        next: A Node object representing the next node in the linked list
    """

    def __init__(self, value):
        """Set-up for the linked list node."""
        self.value = value
        self.next = None

    def __repr__(self):
        """Represents the node as its value as a str."""
        return str(self.value)


def main():
    """Main function call to test union and intersection functions."""
    linked_list_a = LinkedList()
    linked_list_b = LinkedList()
    elements_a = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    elements_b = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for element in elements_a:
        linked_list_a.push(element)

    for element in elements_b:
        linked_list_b.push(element)

    union_set = union(linked_list_a, linked_list_b)
    intersection_set = intersection(linked_list_a, linked_list_b)
    print(union_set)
    print(intersection_set)

    assert str(union_set) == "[32, 9, 11, 1, 2, 35, 65, 6, 4, 3, 21]"
    assert str(intersection_set) == "[6, 4, 21]"

    linked_list_a = LinkedList()
    linked_list_b = LinkedList()
    elements_a = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    elements_b = [1, 7, 8, 9, 11, 21, 1]

    for element in elements_a:
        linked_list_a.push(element)

    for element in elements_b:
        linked_list_b.push(element)

    union_set = union(linked_list_a, linked_list_b)
    intersection_set = intersection(linked_list_a, linked_list_b)
    print(union_set)
    print(intersection_set)

    assert str(union_set) == "[7, 8, 9, 11, 21, 1, 2, 35, 65, 6, 4, 3, 23]"
    assert str(intersection_set) == "[]"

    print("All test cases passed!")


def union(llist_a, llist_b):
    """Creates a linked list that is the union of two linked lists.

    Args:
        llist_a: A LinkedList representing the first list which to create the
            union of
        llist_b: A LinkedList representing the second list which to create the
            union of

    Returns:
        union_set: A LinkedList representing the union of the two given lists
    """
    union_set = LinkedList()
    for llist in (llist_a, llist_b):
        node = llist.head
        while node is not None:
            if not union_set.contains(node.value):
                union_set.push(node.value)

            node = node.next

    return union_set


def intersection(llist_a, llist_b):
    """Creates a linked list that is the intersection of two linked lists.

    Args:
        llist_a: A LinkedList representing the first list which to create the
            intersection of
        llist_b: A LinkedList representing the second list which to create the
            intersection of

    Returns:
        intersection_set: A LinkedList representing the intersection of the two
            given lists
    """
    intersection_set = LinkedList()
    node = llist_a.head
    while node is not None:
        value = node.value
        if llist_b.contains(value) and not intersection_set.contains(value):
            intersection_set.push(value)

        node = node.next

    return intersection_set


if __name__ == "__main__":
    main()
