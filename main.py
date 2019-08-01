# Importing Module
import sys
import requests
import json

#Getting arguments 
length_of_argument = sys.argv
#getting movie name
movie_name = sys.argv[1:]
#Formating movie name
name = "+".join(movie_name)
movie_name1 = " ".join(movie_name)
# Request URL: http://www.omdbapi.com/?t=Blade+runner&apikey=PlzBanMe
#Making Rest API url
api_url = 'http://www.omdbapi.com/?t='+name+'&apikey=PlzBanMe'
# print (length_of_argument[0])
try:
	data_json = requests.get(api_url,timeout=3)
	data_json.raise_for_status()
	if data_json.status_code == 200:

		data_json = str(data_json.text)
		#print(data_json)

		data = json.loads(data_json)
		for i in range(1,len(data['Ratings'])):
			source = data['Ratings'][i]['Source']
			if source == 'Rotten Tomatoes':
				rating_value = data['Ratings'][i]['Value']
				print("Movie Name: " + movie_name1)
				print("Source: Rotten Tomatoes")
				print("Rating: "+rating_value)
				break
	else:
		print(data_json.status_code)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

