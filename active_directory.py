"""Determine is a user is a member of a group.

Usage: active_directory.py

Classes:
    Group()
"""


class Group:
    """Creates a Group object.

    Attributes:
        name: A str representing the name of the group
        groups: A list of group objects representing the groups that are
            members of this group
        users: A list of strs representing the name or ids of the users that
            are members of this group
    """

    def __init__(self, name):
        """Set-up for the Group object."""
        self.name = name
        self.groups = []
        self.users = []

    def __repr__(self):
        """Represents the group as its name."""
        return self.name

    def add_group(self, group):
        """Add a group to the group.

        Args:
            group: A group object representing the group to add to the group
        """
        self.groups.append(group)

    def add_user(self, user):
        """Add a user to the group.

        Args:
            user: A str representing the name or id of the user to add to the
                group
        """
        self.users.append(user)


def main():
    """Main function call to test whether a user is in a group."""
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)

    group_membership_1 = is_user_in_group(sub_child_user, parent)
    print(f"Is user {sub_child_user} in group {parent}: {group_membership_1}")

    group_membership_2 = is_user_in_group("non_group_user", parent)
    print(f"Is user non_group_user in group {parent}: {group_membership_2}")

    assert group_membership_1
    assert not group_membership_2

    print("All test cases passed!")


def is_user_in_group(user, group):
    """Dermines if a user is in a group.

    Args:
        user: A str representing the user name or id to determine if they are a
            member of the given group
        group: A Group object to check if a user is a member of

    Returns:
        A boolean representing if the given user is a member of the given group
    """
    if user in group.users:
        return True

    if len(group.groups) == 0:
        return False

    for sub_group in group.groups:
        if is_user_in_group(user, sub_group):
            return True

    return False


if __name__ == "__main__":
    main()
