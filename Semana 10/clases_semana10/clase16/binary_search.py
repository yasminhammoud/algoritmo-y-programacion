def binary_search(vector, key, keyName=''):
    if len(vector) == 0:
        return None
    mid = len(vector)//2
    if vector[mid].get(keyName) is not None:
        if vector[mid][keyName] == key:
            return vector[mid]
        elif key<vector[mid][keyName]:
            return binary_search(vector[0:mid], key, keyName)
        else: 
            return binary_search(vector[mid+1:], key, keyName) 

