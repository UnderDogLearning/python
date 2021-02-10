def single_letter_count(word, letter):
    lower = word.lower()
    if letter in lower:
        return lower.count(letter)
    else:
        return 0
        
        
"""How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
"""
