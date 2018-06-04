import xlrd
import csv
inputfile=raw_input("Specify path of excel file you want to convert e.g somefile.xlsx\n")
outputfile=raw_input("Specify name of output csv you want e.g newfile.csv\n")
sheetname=raw_input("input name of sheet you want to convert to csv e.g Sheet1\n")
wb = xlrd.open_workbook(inputfile)
sh = wb.sheet_by_name(sheetname)
your_csv_file = open(outputfile, 'w')
wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
for rownum in range(sh.nrows):
	wr.writerow(sh.row_values(rownum))
your_csv_file.close()
