import pandas as pd
data_path= './DATA/FRvideos.csv'


def extract_dislikes():
	nb_dislikes = []
	r = pd.read_csv(data_path)
	r = r.get('dislikes')
	for dislike in r:
		nb_comments.append(dislike)
	return nb_dislikes
extract_dislikes()
