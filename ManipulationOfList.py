def list_manipulation(lst, command, location, value=None):
    command = ['add','remove']
    location = ['starting','end']
    
    if command == 'add':
        if location == 'starting':
            lst.insert(0, value)
            return lst
            
        elif location == 'end':
            lst.append(value)
            return lst
        
        else:
            print("Sorry wrong location")
        
    elif command == 'remove':
        if location == 'starting':
            lst.pop(0)
            return lst
        
        elif location == 'end':
            lst.pop()
            return lst
            
        else:
            print("Sorry Wronf Location")
            return None
     
     else:
        Print("Sorry Wrong Command")
        
        
