def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    n1_st = str(num1)
    n2_st = str(num2)

    count1 = {}
    count2 = {}

    for n in n1_st:
        count1[n] = count1.get(n, 0) + 1
    
    for n in n2_st:
        count2[n] = count2.get(n, 0) + 1

    return count1 == count2