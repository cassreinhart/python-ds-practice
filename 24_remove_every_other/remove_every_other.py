def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    odd_index = 0;
    new_list = []
    
    while odd_index <= len(lst) - 1:
        new_list.append(lst[odd_index])
        odd_index = odd_index + 2

    return new_list