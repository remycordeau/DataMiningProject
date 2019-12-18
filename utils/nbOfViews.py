import pandas as pd
data_path= './DATA/FRvideos.csv'

def getNbOfViews():
	f = pd.read_csv(data_path)
	counter = 0;
	res = []
	for num in f['views']:
		res.append(int(num))
		counter += 1
		if(counter > 2):
			return res

print("Displaying nb of views per video")
res = getNbOfViews()
for i in res:
	print(i)
