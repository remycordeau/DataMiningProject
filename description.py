import pandas as pd
data_path= './DATA/FRvideos.csv'

nb_links = []
nb_word = []
def extract_desc():
	r = pd.read_csv(data_path)
	r = r.get('description')
	for desc in r:
		if desc == desc:
			desc = desc.split()
			cpt_link = 0
			for word in desc:
				if 'http' in word:
				    cpt_link += 1
			nb_links.append(cpt_link)
			nb_word.append(len(desc))
		else:
			nb_links.append(0)
			nb_word.append(0)
	return (nb_links, nb_word)

print(extract_desc())
