"""Return frequency of term in lst"""
def frequency(lst, search_term):
    if search_term in lst:
        num = lst.count(search_term)
        return num
    else:
        return 0
