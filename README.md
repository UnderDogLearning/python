#python
#Reading a file (.csv) using panda
"""Sample data"""

Address	Price	Bedrooms
992 Settled St	823,049	4
1506 Guido St	784,049	3
247 Fort St	299,238	3

import pandas as pd
df = pd.read_csv('filename.csv')
df

---------------------------------------------------
#This provides the index at the starting of the file like below

	Address	Price	Bedrooms
0	992 Settled St	823,049	4
1	1506 Guido St	784,049	3
2	247 Fort St	299,238	3

#we can turn on/off the index by passing the Index=False 

-------------------------------------------------------------------------

#if the data doesnt have a Header 

data = pd.read_csv('filename.csv', sep=",", header=None)
data

-------------------------------------------------------------------

#without pandas 

f = open("demofile.txt", "r")
print(f.read())

---------------------------------

file = open("filename.csv","r")
for line in file:
    print(line)    
file.close()

------------------------------------------
#converting a file from one delimeter to other and want to have few column

file = open("filename.csv","r")
for line in file:
    fields = line.split(",")
    field1 = fields[0]
    field2 = fields[1]    
    print(field1 + "|" + field2 )

---------------------------------

#Wring data into other file:

df.to_csv('homes_inspected.csv')

#Index False while wring to other file:

df.to_csv('homes_inspected.csv', index=False)

---------------------------------------------

#Adding a new column at the end to the current data 

Import panda as pd
df = pd.read_csv(''filename.csv')
df['Inspected'] = 'false'
df.to_csv('homes_inspected.csv', index=False)



