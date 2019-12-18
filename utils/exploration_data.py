import pandas as pd
# A first quick script to explore data-set
data_path= './DATA/FRvideos.csv'

def nb_of_channel():
  r = pd.read_csv(data_path)
  r = r.groupby("channel_title")["title"].aggregate(lambda x: [i for i in x])
  print(r.head(20))
  return(r.size)
  	
print('Exploring ' + data_path + '...') 
print('Number of channel on this data-set : ' + str(nb_of_channel()))
