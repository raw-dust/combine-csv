from os import walk
import csv

mypath =r"C:\Users\Owner\Desktop\csv"
outfile= mypath+"\\"+r"output.csv"

files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)
    breakpoint

#remove output files from list
if "output.csv" in files:
    files.remove("output.csv")

#files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

headerdone = False

fieldnames = set()


print("Geting Field names")
#get field names
for file in files:
    infile = mypath+"\\"+file
    print(infile)
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames.update(reader.fieldnames)
        

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
