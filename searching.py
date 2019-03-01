"""
CSCI-603: Wk 7 Sorting

Implementations of linear and binary search
"""


def search(data, val):
    """
    A linear search for a value in a list.
    :param data: list of data
    :param val: the value to search for
    :return: True if present, False otherwise
    """
    for item in data:
        if item == val:
            return True
    return False


def where(data, val):
    """
    A linear search for a value in a list
    :param data: list of data
    :param val: the value to search for
    :return: The index of the first occurrence of the value, if present,
        -1 otherwise.
    """
    for ind in range(len(data)):
        if data[ind] == val:
            return ind
    return -1


def _binSearchRec(data, val, left, right):
    """
    The recursive binary search function.
    :param data: list of data
    :param val: the value to search for
    :param left: the starting index in data
    :param right: the ending index in data
    :return: The index of the first occurrence of the value, if present,
        -1 otherwise.
    """
    if left > right:
        return -1
    midindex = (left + right) // 2
    if data[midindex] == val:
        return midindex
    if data[midindex] > val:
        return _binSearchRec(data, val, left, midindex - 1)
    else:
        return _binSearchRec(data, val, midindex + 1, right)


def binSearch(data, val):
    """
    The main binary search function, which calls the recursive helper
    function to do the actual search.
    :param data: A list of data
    :param val: The value to search for
    :return: The index of the first occurrence of the value, if present,
        -1 otherwise.
    """
    return _binSearchRec(data, val, 0, len(data) - 1)


def main():
    """
    The main function.
    :return: None
    """
    nums = [4, 7, 2, 1, 8, 3, 6]
    print("5?", search(nums, 5))
    print("1?", search(nums, 1))
    print("5?", where(nums, 5))
    print("1?", where(nums, 1))
    # binary search on unsorted data
    print("binary 1?", _binSearchRec(nums, 1, 0, len(nums) - 1))
    # using the helper function
    print("binary 1?", binSearch(nums, 1))  # why does this work?
    print("binary 2?", binSearch(nums, 2))
    sortednums = [2, 4, 5, 6, 8, 11, 12, 14]
    print("binary 2?", binSearch(sortednums, 2))
    print("binary 7?", binSearch(sortednums, 7))


if __name__ == '__main__':
    main()
