def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    exist = []
    for i, e in enumerate(a):
        if (-e) in dict:
            exist.append(e)
        dict[e] = i
    exist = list(map(abs, exist))
    return exist


if __name__ == "__main__":
    print(has_negatives([1, -1, 2, 3, -4, -3, 4, -5, 6, 7]))
