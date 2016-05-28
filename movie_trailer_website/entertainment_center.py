#import media
#import tmdbsimple as tmdb
from pprint import pprint
from media import *
from fresh_tomatoes import *
import csv

movies_list = []

# Read the movie list information from the csv file
with open('movies_list.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
    	# Append the newly created movie object to the movies_list
    	movies_list.append(Movie(row[0], row[1], row[2], row[3], row[4]))

# Call the open_movies_page funciton
open_movies_page(movies_list)