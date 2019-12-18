import pandas as pd
data_path= './DATA/FRvideos.csv'

def getLowerUpperPercentage():
	f = pd.read_csv(data_path)
	counter = 0;
	res = []
	for title in f['title']:
		upperCaseNb = 0
		lowerCaseNb = 0
		otherChar = 0
		for char in title:
			if char.isupper():
				upperCaseNb += 1
			elif char.islower():
				lowerCaseNb += 1
			else:
				otherChar += 1
		titleLen = float(len(title)-otherChar)
		upperCaseRatio = (upperCaseNb/titleLen)*100
		lowerCaseRatio = (lowerCaseNb/titleLen)*100
		res.append((upperCaseRatio,lowerCaseRatio))
		#print(title+" UP : "+str(upperCaseRatio)+" % LOW : "+str(lowerCaseRatio)+" %")
		counter += 1	
		if(counter > 2):
			return res

print("Computing % of upper/lower case in title")
res = getLowerUpperPercentage()
for i in res:
	print(i)
