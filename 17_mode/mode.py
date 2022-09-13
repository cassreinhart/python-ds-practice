def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_dict = {}

    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    high_num = 1
    
    for (num, count) in num_dict.items():
        if count > high_num:
            high_num = num
    return high_num
