import pandas as pd
data_path= './DATA/FRvideos.csv'


def extract_likes():
	nb_likes = []
	r = pd.read_csv(data_path)
	r = r.get('likes')
	for like in r:
		nb_comments.append(like)
	return nb_likes
extract_likes()
