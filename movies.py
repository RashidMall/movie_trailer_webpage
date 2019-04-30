import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

# Terminator
terminator = media.Movie("Terminator",
                         "A cyborg assassin known as a Terminator arrives from 2029",
                         "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",
                         "https://www.youtube.com/watch?v=fratdVlBiOM")

# School of Rock
school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# Midnight in Paris
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

# Hunger games
hunger_games = media.Movie("Hunger Games",
                           "Storyline",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, terminator, school_of_rock, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
