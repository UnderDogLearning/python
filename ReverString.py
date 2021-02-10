"""Reverse string"""

def reverse_string(phrase):
    arr = list(phrase)
    arr.reverse()
    return ''.join(arr)
    
    
"""Reverse string,
        >>> reverse_string('awesome')
        'emosewa'
        >>> reverse_string('sauce')
        'ecuas'
 """    
