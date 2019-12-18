import pandas as pd
import datetime

tday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
categories ={ 	
	'2' : 'Autos & Vehicles',
	'1' :  'Film & Animation',
	'10' : 'Music',
	'15' : 'Pets & Animals',
	'17' : 'Sports',
	'18' : 'Short Movies',
	'19' : 'Travel & Events',
	'20' : 'Gaming',
	'21' : 'Videoblogging',
	'22' : 'People & Blogs',
	'23' : 'Comedy',
	'24' : 'Entertainment',
	'25' : 'News & Politics',
	'26' : 'Howto & Style',
	'27' : 'Education',
	'28' : 'Science & Technology',
	'29' : 'Nonprofits & Activism',
	'30' : 'Movies',
	'31' : 'Anime/Animation',
	'32' : 'Action/Adventure',
	'33' : 'Classics',
	'34' : 'Comedy',
	'35' : 'Documentary',
	'36' : 'Drama',
	'37' : 'Family',
	'38' : 'Foreign',
	'39' : 'Horror',
	'40' : 'Sci:Fi/Fantasy',
	'41' : 'Thriller',
	'42' : 'Shorts',
	'43' : 'Shows',
	'44' : 'Trailers'
}


def getLowerUpperPercentage(dataFrame):
	lower = []
	upper = []
	for title in dataFrame['title']:
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
		if(len(title) == otherChar):
			titleLen = len(title)
		else:
			titleLen = float(len(title)-otherChar)
		upperCaseRatio = (upperCaseNb/titleLen)*100
		lowerCaseRatio = (lowerCaseNb/titleLen)*100
		upper.append(upperCaseRatio)
		lower.append(lowerCaseRatio)
	return (upper,lower)

def getNbOfTags(dataFrame):
	res = []
	for string in dataFrame['tags']:
		string = string.replace("\"","").split("|")
		if string == '[none]':
			res.append(0)
		else:
			res.append(len(string))
	return res

def getNbOfViews(dataFrame):
	res = []
	for num in dataFrame['views']:
		res.append(num)
	return res

def extract_likes(dataFrame):
	nb_likes = []
	for like in dataFrame['likes']:
		nb_likes.append(like)
	return nb_likes
	
def extract_dislikes(dataFrame):
	nb_dislikes = []
	for dislike in dataFrame['dislikes']:
		nb_dislikes.append(dislike)
	return nb_dislikes	
	
def extract_date(dataFrame):
	day_tab = []
	moment_o_day = []
	nb_dislikes = []
	for date in dataFrame['publish_time']:
		hour = date.split('T')[1]
		date = date.split('T')[0]
		date = date.split('-')
		d= int(date[2])
		m= int(date[1])
		y= int(date[0])
		day = datetime.datetime(y, m, d)
		day = day.weekday()
		day_tab.append(tday[day])
		h = hour.split(':')[0]
		mi = hour.split(':')[1]
		hour = (h + ':' + mi)
		if hour < '11:59':
			moment_o_day.append('morning')
		elif hour >= '12:00' and hour <'19:00':
			moment_o_day.append('afternoon')
		elif hour >= '19:00' and hour <'23:59':
			moment_o_day.append('evening')
	return (day_tab, moment_o_day)	

def extract_comm(dataFrame):
	nb_comments = []
	for count in dataFrame['comment_count']:
		nb_comments.append(count)
	return nb_comments
	
def extract_category(dataFrame):
	cat_tab = []
	for category in dataFrame['category_id']:
		cat_tab.append(categories[str(category)])
	return cat_tab
	
def extract_desc(dataFrame):
	nb_links = []
	nb_word = []
	for desc in dataFrame['description']:
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
		
data_path= './DATA/FRvideos.csv'

def main():
	print("Opening file...")
	f = pd.read_csv(data_path)
	tab = getLowerUpperPercentage(f)
	print("Extracting data from file...")
	tab1 = tab[0]
	tab2 = tab[1]
	tab3 = getNbOfTags(f)
	tab4 = getNbOfViews(f)
	tab5 = extract_likes(f)
	tab6 = extract_dislikes(f)
	tab = extract_date(f)
	tab7 = tab[0]
	tab8 = tab[1]
	tab9 = extract_comm(f)
	tab10 = extract_category(f)
	tab = extract_desc(f)
	tab11 = tab[0]
	tab12 = tab[1]
	print("Writing results in file...")
	csv = open("./DATA/youtubeTrends.csv","w")
	csv.write("index,%upperCase,%lowerCase,nbTags,nbViews,nbLikes,nbDislikes,day,momentOfDay,nbComments,category,nbLinks,nbWords\n")
	for i in range(40703):
		csv.write(str(i)+","+str(tab1[i])+","+str(tab2[i])+","+str(tab3[i])+","+str(tab4[i])+","+str(tab5[i])+","+str(tab6[i])+","+str(tab7[i])+","+str(tab8[i])+","+str(tab9[i])+","+str(tab10[i])+","+str(tab11[i])+","+str(tab12[i])+"\n")
	print("Done.")
	
	
main()

	
