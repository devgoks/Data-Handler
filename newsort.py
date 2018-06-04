import xlsxwriter
WANTED = 15
inputfile=raw_input("Specify file you extracting from e.g somefile.csv\n")
chosen=raw_input("Specify things you want to extract,seperate them with comma\n").split(",")
outputfile=raw_input("specify name of output excel file e.g somefile.xlsx \n")
workbook = xlsxwriter.Workbook(outputfile)
worksheet = workbook.add_worksheet()
row=0
col=0
with open (inputfile) as searchfile:
	for line in searchfile:
		col=0
		for i in chosen:
			if(i=="date"):
        			left,sep,right = line.partition('2018/')
        			if sep:
					worksheet.write(row, col,right[:WANTED])
					col+=1
           				print(right[:WANTED])
			else:
                        	left,sep,right = line.partition(i+'=')
                        	if sep:
           				needed=right.split('&',1)
					worksheet.write(row, col,needed[0])
					col+=1
           				print(needed[0])
		row+=1
workbook.close()

