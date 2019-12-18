import pandas as pd
import datetime

data_path= './DATA/FRvideos.csv'

day = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

def extract_date():
	day_tab = []
	moment_o_day = []
	nb_dislikes = []
	r = pd.read_csv(data_path)
	r = r.get('publish_time')
	for date in r:
		hour = date.split('T')[1]
		date = date.split('T')[0]
		date = date.split('-')
		d= int(date[2])
		m= int(date[1])
		y= int(date[0])
		day = datetime.datetime(y, m, d)
		day = day.weekday()
		day_tab.append(day)
		h = hour.split(':')[0]
		mi = hour.split(':')[1]
		hour = (h + ':' + mi)
		if hour < '11:59':
			moment_o_day.append('matin')
		elif hour >= '12:00' and hour <'19:00':
			moment_o_day.append('après-midi')
		elif hour >= '19:00' and hour <'23:59':
			moment_o_day.append('soir')
	return (day_tab, moment_o_day)
print(extract_date())
