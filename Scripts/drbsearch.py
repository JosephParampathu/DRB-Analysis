#using numpy for matrices
from os import listdir
from os.path import isfile, join
#import numpy


mypath = "/Users/josephparampathu/Desktop/Programming/DRBanalysis/ExcelPythonScript/DRB 2017"
#This creates a list of file titles, without the file extension
onlyfiles = [filename[0:filename.index(".")] for filename in listdir(mypath)
                if isfile(join(mypath, filename))]


#Check each file for the strings "grant", "deny", and "liberal consideration" return 1 or 0
onlygrants = []
onlydenies = []
onlymentalhealth = []

for filename in listdir(mypath):
    myfile = open(mypath+"/"+filename)
    if('grant' in myfile.read()):
        onlygrants.append(1)
    else:
        onlygrants.append(0)
    if('deny' in myfile.read()):
        onlydenies.append(1)
    else:
        onlydenies.append(0)
    if('liberal consideration' in myfile.read()):
        onlymentalhealth.append(1)
    else:
        onlymentalhealth.append(0)
    myfile.close()
