"""
Media.py is where we define the class that will be used and be instantiated
from entertainment_center.py file
"""

# Define a class Movie that take 3 attribute of a movie as parameters
# Its title, its poster image, and its trailer url


class Movie:
    def __init__(me, movie_title, poster_url, movie_trailer_url):
        me.title = movie_title
        me.poster_image_url = poster_url
        me.trailer_youtube_url = movie_trailer_url
