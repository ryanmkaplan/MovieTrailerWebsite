import fresh_tomatoes
import media

#
# Source data for my favorite movies and add them to the to the instance of the Movie class
#

stepbros = media.Movie("Step Brothers",
                     "Two grown men becoming step brothers",
                     "Rating: R",
                     "http://ia.media-imdb.com/images/M/MV5BMTcwNzUzMjU1OV5BMl5BanBnXkFtZTcwMTM0NDQ2MQ@@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=ANjenc4W1_Q")

fourty_year_old_virgin = media.Movie("40 Year Old Virgin",
                     "40 year old single man is looking to loose his virginity",
                     "Rating: R",
                     "http://ia.media-imdb.com/images/M/MV5BMTU5MzU2MzY2Nl5BMl5BanBnXkFtZTgwOTM4NzMxMDE@._V1_SY317_CR0,0,214,317_AL_.jpg",

                     "https://www.youtube.com/watch?v=hysIlCVLejk")

good_will_hunting = media.Movie("Good Will Hunting",
                     "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
                     "Rating: R",
                     "http://ia.media-imdb.com/images/M/MV5BMTk0NjY0Mzg5MF5BMl5BanBnXkFtZTcwNzM1OTM2MQ@@._V1_SY317_CR1,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=WDcMUCpppVs")

fast_n_furious = media.Movie("The Fast and The Furious",
                     "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
                     "Rating: PG-13",
                     "http://ia.media-imdb.com/images/M/MV5BMjAwNTQ0Nzc2M15BMl5BanBnXkFtZTcwNTk1MDIwNA@@._V1_SX214_AL_.jpg",
                     "www.youtube.com/watch?v=ZsJz2TJAPjw")

#
# For testing purposes only. this can be used to print differnt attributes
#
#print(stepbros.storyline)
#stepbros.show_trailer()

#
# load movies into the movies array and call fresh_tomatoes to display the
# webpage with movie images and once play the youtube video trailer if clicked
#
movies = [stepbros, fourty_year_old_virgin, good_will_hunting, fast_n_furious]
fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
#print(media.Movie.__name__)
