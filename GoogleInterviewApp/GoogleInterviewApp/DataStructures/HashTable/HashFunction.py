def hashFunction(param, size):
    hash_value = 0
    for i in range(len(param)):
        hash_value = (hash_value + ord(param[i]) * i) % size

    return hash_value