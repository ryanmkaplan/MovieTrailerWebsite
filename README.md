# MovieTrailerWebsite
This program allows users to view my favorite movies and watch the trailers. It's writeen in Python, with side code to store a list of movie titles, box art, poster images, and movie trailer URLs. The data is expressed on the web page and allow users to review the movies and watch the trailers.

# Tech Stack

Python 2

# Python Modules

Webbrowser
Os
Re

# Fresh_Tomatoes.py

contains the open_movies_page() function that takes my list of movies and generate an HTML file including this content, producing a website to showcase your favorite movies.

# Media.py

contains a class Movie that holds the different proprties of the movie file: movie_title, movie_storyline, poster_image, trailer_youtube and can also call the browser to open the trailer

# entertainment_center.py

The location of the movies list by calling the media.Movie() to instantiate the movie objects
