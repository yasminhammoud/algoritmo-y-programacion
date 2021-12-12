def linear_search(vector, key, keyName=''):
    temp = None
    for element in vector:
        if element.get(keyName) is not None:
            if element[keyName] == key:
                temp = element
                break 
    return temp 
     