def string_bits(str):
"""
Given a string, return a new string made of every 
other char starting with the first, so "Hello" yields
"Hlo"
"""
    b = ""
    for i in range(len(str)):
        if (i%2)==0: 
            b += str[i]
    return b 