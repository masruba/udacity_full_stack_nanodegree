# Quick-Start

## Steps to run the application

### Open a terminal and run the following command:

```
python entertainment_center.py 
```

A html file named (fresh_tomatoes.html) will be opened in your browser.

### Optional 

- I have used Movie DB API (https://www.themoviedb.org/documentation/api) to get the movie data. In order to run this step, you'll need to get API Key from the Movie DB website. And, You'll use your own API Key in `generate_data.py`.

```
# TODO: Use your own API Key 
API_KEY = 'USE_YOUR_API_KEY'
```

- Open a terminal and run the following command to generate the data again
```
python generate_data
```
After running the above command, the movie data will be written to movies_list.csv file. Then, as usual, you have to run the following command to generate the html file.

```
python entertainment_center.py 
```

### Brief File Description

- entertainment_center.py : Read the movies data from the movies_list.csv file and create Movie objects. 
- media.py: Contains Movie Class
- generate_data.py: Get the data from the Movie DB API and write the data to a csv file named movies_list.csv (default) file
- fresh_tomatoes.py: Fun functionality: Hovering any item will show the overview of that movie