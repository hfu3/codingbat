def string_splosion(str):
    
    # for i in len(str): 
    #     return i*str[0:i]

    result = ""
    for i in range(len(str)): 
        result = result + str[:i+1]
    return result