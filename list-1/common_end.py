def common_end(a, b):
"""
Given 2 arrays of ints, a and b, return True if they 
have the same first element or they have the same last
 element. Both arrays will be length 1 or more.
"""
if a[0] == b[0] and a[-1] == b[-1]:
    return True 
else: 
    return False