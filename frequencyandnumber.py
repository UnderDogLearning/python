def frequency(lst, search_term):
    if search_term in lst:
        print(f"the {search_term} is present in {lst}")
        num = lst.count(search_term)
        print(f"the number of times the {search_term} is in the {lst} is {num} times") 
    else:
        return 0
        
        
 frequency([1, 4, 3, 4, 4], 4)
 
