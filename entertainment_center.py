'''
This entertainment_center.py file contains some instances of class Movie
and also as a constructor for fresh_tomatoes.html
'''
import media            # import media.py file
import fresh_tomatoes   # import fresh_tomatoes.py file

# Instantiate some movie objects that pass 3 parameters to class Movie
# that follows the class parameter sequence, except 'self'
spiderman = media.Movie(
    "Spiderman: Homecoming",
    "http://cinemaxx.cinemaxxtheater.com/Gallery/Movies/Thumbnail/Spider-Man-Homecoming%20(2).jpg",    # NOQA
    "https://www.youtube.com/watch?v=U0D3AOldjMU"
    )

avenger = media.Movie(
    "The Avengers",
    "http://img02.deviantart.net/9fdb/i/2012/350/9/5/marvel_the_avengers_poster_by_casval_lem_daikun-d5o8dwa.jpg",    # NOQA
    "https://www.youtube.com/watch?v=eOrNdBpGMv8"
    )

minions = media.Movie(
    "Minions",
    "http://s3.amazonaws.com/kidzworld_photo/images/2014114/f87b8d1f-975b-4e93-a565-aa478c6423a7/minions-poster.jpg",    # NOQA
    "https://www.youtube.com/watch?v=7AFUch5JZaQ"
    )

despicable_me_2 = media.Movie(
    "Despicable Me 2",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3NjY0MTQ0Nl5BMl5BanBnXkFtZTcwMzQ2MTc0Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",    # NOQA
    "https://www.youtube.com/watch?v=yM9sKpQOuEw"
    )

boss_baby = media.Movie(
    "The Boss Baby",
    "http://i0.kym-cdn.com/entries/icons/original/000/022/861/the-boss-baby.70675.jpg",    # NOQA
    "https://www.youtube.com/watch?v=tquIfapGVqs"
    )

sherlock_holmes = media.Movie(
    "Sherlock Holmes: A Game of Shadows",
    "https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/sherlock_holmes_game_of_shadows_keyart.jpg?itok=HYrLe-4v",    # NOQA
    "https://www.youtube.com/watch?v=td2Zjdjqhhs"
    )

percy_jackson = media.Movie(
    "Percy Jackson & The Lightning Thief",
    "https://i.ytimg.com/vi/Q1z8OVfAUCI/movieposter.jpg",
    "https://www.youtube.com/watch?v=cil-VXYW6sA"
    )

# Create a list that contains all of the instances
movies_list = [spiderman, avenger, minions, despicable_me_2, boss_baby,
               sherlock_holmes, percy_jackson]

# Call a function from fresh_tomatoes.py and open the website that we create
# and takes movie_list list as an argument
fresh_tomatoes.open_movies_page(movies_list)
