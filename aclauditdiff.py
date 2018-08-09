#

import csv

f1 = file('file.csv', 'r')
f2 = file('file2.csv', 'r')
f3 = file('output.csv, 'w')

#importa and parse assocaite file that should be a CSV in following format
# will call this sAssoc
sAssoc = csv.reader(f1)

#import and parse application ACL file
sApp = csv.reader(f2)

#Output file
sOutput = csv.writer(f3)

#function to compare and append to outputfile
masterlist = list(set(sAssoc) - set(sApp))

c3.writelist(masterList)

f1.close()
f2.close()
f3.close()
