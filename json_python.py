#handling Json data using python

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON string:
y = json.dumps(x)
# convert json string to Json Dict
jsonDict = json.loads(y)
print(jsonDict)
print(jsonDict['name'])

#output
{'name': 'John', 'age': 30, 'city': 'New York'}
John

# wring the data into a file:
with open('data.txt', 'w') as outfile:
    json.dump(x, outfile)
    
#file:
{"name": "John", "age": 30, "city": "New York"}


###
import json

data = {
'bill': 'tech',
'federer': 'tennis',
'ronaldo': 'football',
'people' : [ {
'name': 'Scott',
'website': 'stackabuse.com',
'from': 'Nebraska'}, 
{'name': 'Larry',
'website': 'google.com',
'from': 'Michigan' } ]
}

with open('data1.txt', 'w') as outfile:
    json.dump(data, outfile)
    
    
import json

with open('data1.txt') as json_file:
    data = json.load(json_file)
    print ("bill:", data['bill'])
    print ("")
    for person in data['people']:
        print("Name:", person['name'])
        print("Website:", person['website'])
        print("From:", person['from'])
        print("")
        
        
#OUTPUT::
bill: tech

Name: Scott
Website: stackabuse.com
From: Nebraska

Name: Larry
Website: google.com
From: Michigan


# Formating the data present in the script

import json

data = {
'bill': 'tech',
'federer': 'tennis',
'ronaldo': 'football',
'people' : [ {
'name': 'Scott',
'website': 'stackabuse.com',
'from': 'Nebraska'}, 
{'name': 'Larry',
'website': 'google.com',
'from': 'Michigan' } ]
}

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
    print(json.dumps(data, indent=4))
    
---------------------------------------------   
    
#format the data in a jason file:   
import json

with open('data1.txt') as outfile1:
    datafinal = json.load(outfile1)
    print(json.dumps(datafinal, indent=4))
    
    
----------------------------------------------
# Handing the Json nested file:
#work with complex Json and extract data from it

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
