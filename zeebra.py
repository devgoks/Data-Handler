import re
inputfile=input("Enter name of file you want to format\n")
outputfile=input("Enter name of output file\n")
#things we want to filter out from file content
table = str.maketrans(dict.fromkeys('+\n '))
#read file contents
file=open(inputfile, "r")
prin=file.readlines()
file.close()
#using pattern to track numbers that start with 0 for 080*** to change them to 23480***
pattern=r"^0"
#open output file for write
outputfile_content=open(outputfile,"w")
for i in prin:
#remove + \n from each line of input file content and writes to output file
  filterfile=i.translate(table)
  if re.match(pattern,i):
    outputfile_content.write("'%s'," % re.sub(pattern, "234", filterfile))
  else:
    outputfile_content.write("'%s'," % filterfile)
outputfile_content.close()
  
    
