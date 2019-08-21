#importing Modules
import sys
import requests
import json

class MovieRating:
    #defining API data
    api_key = 'b1c41fdf'
    #Defining Link url
    api_url = 'http://www.omdbapi.com'


    def __init__(self, movie_name):
        self.movie_name = movie_name
        self.data = {}

    def validation(self):
        self.payload = {'t': self.movie_name, 'r': 'json', 'apikey': MovieRating.api_key}
        try:
            self.data = requests.get(MovieRating.api_url, params=self.payload,timeout=3).json()
            return self.data
        #Checkinh HTTP error
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        #Checkinh ConnectionError error
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        #Checkinh Timeout error
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        #Checkinh error apart from mentioned above
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        return self.data

    def get_result(self):
        data = self.validation()
        try:
            if('Ratings' in data):
                for i in range(1,len(data['Ratings'])):
                    source = data['Ratings'][i]['Source']
                    if source == 'Rotten Tomatoes':
                        rating_value = data['Ratings'][i]['Value']
                        print("Movie Name: " + str(self.movie_name))
                        print("Source: Rotten Tomatoes")
                        print("Rating: "+rating_value)
                        break
            else:
                print("Movie Name: " + str(self.movie_name))
                value =  data['Error']
                print ("Error: " +value)
        except KeyError:
            pass
        except IndexError:
            print ("Ratings not avialable")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('Please provide movie name as an argument')
    else:
        rating = MovieRating(sys.argv[1:])
        rating.get_result()
