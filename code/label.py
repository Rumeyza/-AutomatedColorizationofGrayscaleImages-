import os
import random

all_files = os.listdir("data//RawData")
random.shuffle(all_files)

if ".DS_Store" in all_files:
	all_files.remove(".DS_Store")
#print(all_files)

count = len(all_files)
output= open("train_labels.txt",'w')
last_index = 0 
for i in range(int(count*0.8)):
	if(all_files[i].startswith("Forest")):
		output.write(all_files[i]+",0\n")
	elif(all_files[i].startswith("Highway")):
		output.write(all_files[i]+",1\n")
	elif(all_files[i].startswith("Landscape")):
		output.write(all_files[i]+",2\n")
	elif(all_files[i].startswith("Landwater")):
		output.write(all_files[i]+",3\n")
	elif(all_files[i].startswith("Mountain")):
		output.write(all_files[i]+",4\n")
	elif(all_files[i].startswith("OpenCountry")):
		output.write(all_files[i]+",5\n")
	elif(all_files[i].startswith("Street")):
		output.write(all_files[i]+",6\n")
	else:
		output.write(all_files[i]+",7\n")
	last_index = i

output2= open("test_labels.txt",'w') 

for i in range(last_index+1 ,count):
	if(all_files[i].startswith("Forest")):
		output2.write(all_files[i]+",0\n")
	elif(all_files[i].startswith("Highway")):
		output2.write(all_files[i]+",1\n")
	elif(all_files[i].startswith("Landscape")):
		output2.write(all_files[i]+",2\n")
	elif(all_files[i].startswith("Landwater")):
		output2.write(all_files[i]+",3\n")
	elif(all_files[i].startswith("Mountain")):
		output2.write(all_files[i]+",4\n")
	elif(all_files[i].startswith("OpenCountry")):
		output2.write(all_files[i]+",5\n")
	elif(all_files[i].startswith("Street")):
		output2.write(all_files[i]+",6\n")
	else:
		output2.write(all_files[i]+",7\n")

output.close