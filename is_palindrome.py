def is_palindrome(pharse):
    lowercase = pharse.lower().replace(' ','')
    list_lowercase = list(lowercase)

    reverselist = list(lowercase)
    reverselist.reverse()

    for i in range(len(list_lowercase)):
        if lowercase[i] != reverselist[i]:
            return False
        else:
            return True


is_palindrome("HE  LLO")
