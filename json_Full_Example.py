json Example:

x = {
  "company_number": "12345678",
  "data": {
    "address": {
      "address_line_1": "Address 1",
      "locality": "Henley-On-Thames",
      "postal_code": "RG9 1DP",
      "premises": "161",
      "region": "Oxfordshire"
    },
    "country_of_residence": "England",
    "date_of_birth": {
      "month": 2,
      "year": 1977
    },
    "etag": "26281dhge33b22df2359sd6afsff2cb8cf62bb4a7f00",
    "kind": "individual-person-with-significant-control",
    "links": {
      "self": "/company/12345678/persons-with-significant-control/individual/bIhuKnFctSnjrDjUG8n3NgOrl"
    },
    "name": "John M Smith",
    "name_elements": {
      "forename": "John",
      "middle_name": "M",
      "surname": "Smith",
      "title": "Mrs"
    },
    "nationality": "Vietnamese",
    "natures_of_control": [
      "ownership-of-shares-50-to-75-percent"
    ],
    "notified_on": "2016-04-06"
  }
}

import json

# convert into JSON string:
y = json.dumps(x)
# convert json string to Json Dict
jsonDict = json.loads(y)


print(jsonDict)


with open('data.txt', 'w') as outfile:
    json.dump(x, outfile)
    print(json.dumps(x, indent=6))
    
    
print(jsonDict['company_number'])
>>12345678

print(jsonDict['data'])
>>{'address': {'address_line_1': 'Address 1', 'locality': 'Henley-On-Thames', 'postal_code': 'RG9 1DP', 'premises': '161', 'region': 'Oxfordshire'}, 'country_of_residence': 'England', 'date_of_birth': {'month': 2, 'year': 1977}, 'etag': '26281dhge33b22df2359sd6afsff2cb8cf62bb4a7f00', 'kind': 'individual-person-with-significant-control', 'links': {'self': '/company/12345678/persons-with-significant-control/individual/bIhuKnFctSnjrDjUG8n3NgOrl'}, 'name': 'John M Smith', 'name_elements': {'forename': 'John', 'middle_name': 'M', 'surname': 'Smith', 'title': 'Mrs'}, 'nationality': 'Vietnamese', 'natures_of_control': ['ownership-of-shares-50-to-75-percent'], 'notified_on': '2016-04-06'}

# convert into JSON string:
FinalData = json.dumps(jsonDict['data'])
# convert json string to Json Dict
FD = json.loads(FinalData)
print(FD)

>> {'address': {'address_line_1': 'Address 1', 'locality': 'Henley-On-Thames', 'postal_code': 'RG9 1DP', 'premises': '161', 'region': 'Oxfordshire'}, 'country_of_residence': 'England', 'date_of_birth': {'month': 2, 'year': 1977}, 'etag': '26281dhge33b22df2359sd6afsff2cb8cf62bb4a7f00', 'kind': 'individual-person-with-significant-control', 'links': {'self': '/company/12345678/persons-with-significant-control/individual/bIhuKnFctSnjrDjUG8n3NgOrl'}, 'name': 'John M Smith', 'name_elements': {'forename': 'John', 'middle_name': 'M', 'surname': 'Smith', 'title': 'Mrs'}, 'nationality': 'Vietnamese', 'natures_of_control': ['ownership-of-shares-50-to-75-percent'], 'notified_on': '2016-04-06'}

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
    

for element in FD:
  #If Json Field value is a Nested Json
    if (isinstance(FD[element], dict)):
        checkDict(FD[element], element)
    #If Json Field value is a list
    elif (isinstance(FD[element], list)):
        checkList(FD[element], element)
    #If Json Field value is a string
    elif (isinstance(FD[element], str)):
        printField(FD[element], element)
        
>>
address.address_line_1 : Address 1
address.locality : Henley-On-Thames
address.postal_code : RG9 1DP
address.premises : 161
address.region : Oxfordshire
country_of_residence : England
etag : 26281dhge33b22df2359sd6afsff2cb8cf62bb4a7f00
kind : individual-person-with-significant-control
links.self : /company/12345678/persons-with-significant-control/individual/bIhuKnFctSnjrDjUG8n3NgOrl
name : John M Smith
name_elements.forename : John
name_elements.middle_name : M
name_elements.surname : Smith
name_elements.title : Mrs
nationality : Vietnamese
natures_of_control[0] : ownership-of-shares-50-to-75-percent
notified_on : 2016-04-06


##Otherway of filterning 


