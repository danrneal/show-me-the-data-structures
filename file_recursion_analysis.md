# File Recursion

## Design Choices

The function find_files just uses simple recursion to traverse the file structure and check each file once.

## Time Complexity

Each file is checked once so the time complexity grows with the size of the file structure meaning time complexity is O(n) in all cases.

## Space Complexity

The files with the correct extension are simply stored in a list so space complexity is O(n) in the worst case (i.e. all files have the specified extension).
