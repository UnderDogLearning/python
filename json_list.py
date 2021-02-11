#Python_json_list

import json

data= [
    {
        "title": "Baby (Feat. Ludacris) - Justin Bieber",
        "description": "Baby (Feat. Ludacris) by Justin Bieber on Grooveshark",
        "link": "http://listen.grooveshark.com/s/Baby+Feat+Ludacris+/2Bqvdq",
        "pubDate": "Wed, 28 Apr 2010 02:37:53 -0400",
        "pubTime": "1272436673",
        "TinyLink": "http://tinysong.com/d3wI",
        "SongID": "24447862",
        "SongName": "Baby (Feat. Ludacris)",
        "ArtistID": "1118876",
        "ArtistName": "Justin Bieber",
        "AlbumID": "4104002",
        "AlbumName": "My World (Part II);\nhttp://tinysong.com/gQsw",
        "LongLink": "11578982",
        "GroovesharkLink": "11578982",
        "Link": "http://tinysong.com/d3wI"
    },
    {
        "title": "Feel Good Inc - Gorillaz",
        "description": "Feel Good Inc by Gorillaz on Grooveshark",
        "link": "http://listen.grooveshark.com/s/Feel+Good+Inc/1UksmI",
        "pubDate": "Wed, 28 Apr 2010 02:25:30 -0400",
        "pubTime": "1272435930"
    }
]

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
    
y = json.dumps(data)
# convert json string to Json Dict
jsonDict = json.loads(y)

record = 0
#print(jsonDict)
for element in jsonDict:
    
    #print(jsonDict[i])
    print("""""")
    print(record)
    record += 1
    #print(element)
    if (isinstance(element, dict)):
        #print("YES")
        #print(element)
        for i in element:      
            if (isinstance(element[i], str)):      
                printField(element[i], i)           
    else:
        print("GONE")
