
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    
    # loop through list
    for i in range(length):
        # store each weight as key
        weight = weights[i]
        # if weight in cache
        if weight in cache:
            # store weight in cache as value
            value = cache[weight]
            # return tuple with (index, value)
            return (i, value)
        # determine difference 
        diff = limit - weight
        # add to diff to cache as i
        cache[diff] = i
        
    return None
    
