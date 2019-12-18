import pandas as pd
data_path= './DATA/FRvideos.csv'

def getNbOfTags():
	f = pd.read_csv(data_path)
	counter = 0;
	res = []
	for string in f['tags']:
		string = string.replace("\"","").split("|")
		print(string)
		if string == '[none]':
			res.append(0)
		else:
			res.append(len(string))
		counter += 1
		if(counter > 2):
			return res

print("Displaying nb of tags per video")
res = getNbOfTags()
for i in res:
	print(i)
