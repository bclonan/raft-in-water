def transform_list_to_2d_array(one_d_list):
    if len(one_d_list) != 10000:
        raise ValueError("List must contain 10,000 integers.")
    return [one_d_list[i:i+100] for i in range(0, 10000, 100)]
