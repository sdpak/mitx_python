def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    firstone = mIncreasing(L)
    secondone = mDecreasing(L)
    result = 0
    if len(firstone) > len(secondone) :
        for i in firstone:
            result += i
    elif len(firstone) == len(secondone) :
        for i in L:
            if sum(firstone) == sum(secondone):
                for r in firstone:
                    result += r
                break
            if i in firstone and not i in secondone:
                for j in firstone:
                    result += j
                break
            elif i in secondone and not i in firstone:
                for k in secondone:
                    result += k
                break

    elif len(firstone) < len(secondone):
        for i in secondone:
            result += i
    return result