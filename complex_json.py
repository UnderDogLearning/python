# Handing the Json nested file:
#work with complex Json and extract data from it
#Iterate through Json data which has list, json string, nested Json. Here I will explain how to work with complex Json and extract data from it


import json

def checkList(ele, prefix):
    for i in range(len(ele)):
        if (isinstance(ele[i], list)):
            checkList(ele[i], prefix+"["+str(i)+"]")
        elif (isinstance(ele[i], str)):
            printField(ele[i], prefix+"["+str(i)+"]")
        else:
            checkDict(ele[i], prefix+"["+str(i)+"]")

def checkDict(jsonObject, prefix):
    for ele in jsonObject:
        if (isinstance(jsonObject[ele], dict)):
            checkDict(jsonObject[ele], prefix+"."+ele)

        elif (isinstance(jsonObject[ele], list)):
            checkList(jsonObject[ele], prefix+"."+ele)

        elif (isinstance(jsonObject[ele], str)):
            printField(jsonObject[ele],  prefix+"."+ele)

def printField(ele, prefix):
    print (prefix, ":" , ele)


data = {'field1': 'hello1',
        'field2': 'hello2',
        'NestedJson': {'Field': 'helloNested1',
                       'List': [{'f01': 'v01', 'f02': 'v02'},
                                          {'f11': 'v11'}],
                       'NestedNestedJson': {'Field1': 'value1',
                                            'Field2': 'value2'}
                        },
        'List': [{'a1': 'b1'},
                 {'a1': 'b1'}],
        'ElementList': ['ele1', 'ele2', 'ele3']
        }
        
# if data is in the file then:
"""with open('data1.txt') as outfile1:
    data = json.load(outfile1)"""
    

#Iterating all the fields of the JSON
for element in data:
  #If Json Field value is a Nested Json
    if (isinstance(data[element], dict)):
        checkDict(data[element], element)
    #If Json Field value is a list
    elif (isinstance(data[element], list)):
        checkList(data[element], element)
    #If Json Field value is a string
    elif (isinstance(data[element], str)):
        printField(data[element], element)
