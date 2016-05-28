from pprint import pprint
import requests
import json
from datetime import datetime
import csv

# TODO: Get your API_KEY from https://www.themoviedb.org/documentation/api?language=en
API_KEY = 'USE_YOUR_API_KEY'

def query_movie_db_api(url, params):
	r = requests.get(url, params=params)
	info = json.loads(r.text)
	return info['results']

# Get the youtube url given a movie id
def get_youtube_url(movie_id, params):
	base_url = "http://api.themoviedb.org/3/movie/"
	url = base_url + str(movie_id) + "/videos?"
	r = requests.get(url, params=params)
	info = json.loads(r.text)

	# Return the youtube video link
	return "https://www.youtube.com/watch?v=" + info['results'][0]['key']

# Write the data to a csv file
def write_popular_movies_list(csv_file_name='movies_list.csv'):
	# Get the most popular movies from the movie db API
	url = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc"
	params = {"api_key": API_KEY}
	
	# Get the list
	movies_info_list = query_movie_db_api(url, params)
	# Limit the list to 12
	movies_info_list = movies_info_list[0:12]

	# Write the movie data to a csv file
	with open(csv_file_name, 'wb') as csvfile:
		writer = csv.writer(csvfile)
		movies_list = []

		# traverse the movies info list
		for movie in movies_info_list:
			title = movie['title']
			movie_id = movie['id']
			# Only the Year is parsed 
			release_year = datetime.strptime(movie['release_date'], '%Y-%m-%d').year

			# Construct the poster_url
			poster_url = "http://image.tmdb.org/t/p/w500/" + movie['poster_path']

			# Get the youtube url for a given movie id
			trailer_url = get_youtube_url(movie_id, params)

			# Write the row
			writer.writerow([title, release_year, poster_url, trailer_url, 
												movie['overview'].encode('ascii', 'ignore')])

if __name__ == "__main__":
	write_popular_movies_list()