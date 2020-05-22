# Active Directory

## Design Choices

The is_user_in_group checks if the user is in the given group and then performs the same check on the subgroups using recursion.

## Time Complexity

This function will traverse the entire subgroup structure checking each subgroup once for the given user so therefore the time complexity is O(n).

## Space Complexity

No data is stored in any data structure except for variables and the function just returns a simple boolean value so the space complexity is a constant O(1).
