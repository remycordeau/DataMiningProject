import pandas as pd
data_path= './DATA/FRvideos.csv'


def extract_comm():
	nb_comments = []
	r = pd.read_csv(data_path)
	r = r.get('comment_count')
	for word in r:
		nb_comments.append(word)
	return nb_comments
extract_comm()
