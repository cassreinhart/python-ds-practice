def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    
    TL_BR = []
    n = 0

    for l in matrix:
        
        TL_BR.append(l[n])
        n = n + 1
    
    BL_TR = []
    n = len(matrix) - 1
    for l in matrix:

        BL_TR.append(l[n])
        n = n - 1
    
    new_list = TL_BR + BL_TR

    return sum(new_list)