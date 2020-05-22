"""Find all files beneath a given path with a given file name suffix.

Usage: file_recursion.py
"""

import os


def main():
    """Main function call to test the find_files function."""
    files = find_files(".c", "testdir")
    print(files)
    assert files == [
        "testdir/subdir5/a.c",
        "testdir/subdir3/subsubdir1/b.c",
        "testdir/subdir1/a.c",
        "testdir/t1.c",
    ]

    print("All test cases passed!")


def find_files(suffix, path):
    """Find all files beneath path with file name suffix.

    Args:
        suffix: A str representing the suffix of the file name to be found
        path: A str representing the path of the file system

    Returns:
        file_list: A list of strs representing paths of files with the given
            suffix
    """
    file_list = []

    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isfile(entry_path) and entry.endswith(suffix):
            file_list.append(entry_path)
        if os.path.isdir(entry_path):
            file_list += find_files(suffix, entry_path)

    return file_list


if __name__ == "__main__":
    main()
