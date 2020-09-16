def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {}
    for (index, weight) in enumerate(weights):
        limit_minus_weight = limit - weight
        if limit_minus_weight in weight_dict:
            return (index, weight_dict[limit_minus_weight])
        weight_dict[weight] = index
    
    return None

