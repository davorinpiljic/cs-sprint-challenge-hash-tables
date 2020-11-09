def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    for i, e in enumerate(weights):
        if limit - e in dict:
            print([dict.get(limit - e), i])
            return ([dict.get(limit - e), i])
        dict[e] = i
        print(dict)


weights = [45, 35, 135, 25, 10, 5]
get_indices_of_item_weights(weights, len(weights), 145)
