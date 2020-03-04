def pair_sum(arr, k):
    """
    finds all the unique pairs in an array that sum up to a given k value
    :param arr:
    :param k:
    :return: print pairs
    """
    if len(arr) < 2:
        print('Too small')

    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((num, target))

    print('\n'.join(map(str, list(output))))


pair_sum([1, 3, 5, 4, 0], 4)
