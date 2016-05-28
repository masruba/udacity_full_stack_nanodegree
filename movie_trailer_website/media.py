class Movie():
	# Movie Class Constructor
	def __init__(self, title="", release_year="", poster_url="", 
										 youtube_url="", overview=""):
		self.title = title
		self.release_year = release_year
		self.poster_image_url = poster_url
		self.trailer_youtube_url = youtube_url
		self.overview = overview
