#
import csv
import xlrd

#HR can provide a xlsx file. Can take file name in as variable in future
# For now rename to HRReport.xlsx
#HR Report, Col #15(O) is the email
workbook = xlrd.open_workbook("HRReport.xls")
sheet = workbook.sheet_by_index(0)

for rowx in range(sheet.nrows):
    cols = sheet.row_values(rowx)
    print(cols)


#import and parse Assocaite CSV file
# will call this lAssociates
with open('AssocList.csv', 'r') as f1:
  reader = csv.reader(f1)
  lAssociates = []
  for row in reader:
    lAssociates.append(row[0])


#import and parse Application.ACL  CSV
# will call this lApplicationacl
with open('ApplicationACL.csv', 'r') as f2:
  reader = csv.reader(f2)
  lApplicationacl = []
  for row in reader:
    lApplicationacl.append(row[0])

#print(lAssociates)
#print(lApplicationacl)

#Output file
#sOutput = csv.writer(f3)

#function to compare and append to outputfile
#convert lists to sets
sAssociates = set(lAssociates)
sApplicationacl = set(lApplicationacl)

masterlist = list(set(sAssociates) - set(sApplicationacl))
print(masterlist)

#f3 = file('output.csv', 'wb')
#wo = csv.writer(f3, dialect='excel')
#for item in masterlist:
#    wo.writerow(item)
with open("output.csv",'wb') as resultFile:
  wr = csv.writer(resultFile, dialect='excel')
  wr.writerows(masterlist)

#f3.writelines(masterlist)

#close the files uopadated
f1.close()
f2.close()
resultFile.close()


