from os import walk
import csv

mypath =r"C:\DIRECTORY\CONTAINING\CSV\FILES"
outfile= mypath+"\\"+r"output.csv"

files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)
    breakpoint

#remove output files from list
if "output.csv" in files:
    files.remove("output.csv")


headerdone = False

fieldnames = []


print("Geting Field names")
#get field names
for file in files:
    infile = mypath+"\\"+file
    print(infile)
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        currentfields = reader.fieldnames
        for currentfield in currentfields:
            if currentfield not in fieldnames:
                fieldnames.append(currentfield)

print("Writing file")
with open(outfile, 'w', newline='') as outcsvfile:    
    writer = csv.DictWriter(outcsvfile, fieldnames=fieldnames)
    writer.writeheader()

    for file in files:
        infile = mypath+"\\"+file
        print(infile)
        with open(infile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                writer.writerow(row)


        
                


