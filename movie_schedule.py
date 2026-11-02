
movie_schedule = {
    "Inception": "7:00 PM",
    "The Matrix": "8:30 PM",
    "Interstellar": "9:00 PM",
    "The Dark Knight": "6:45 PM",
    "Pulp Fiction": "8:00 PM",
}

print("Welcome: Below are some of the available Movies")
for movie in movie_schedule:
    print(movie)

user_request = input("Please enter the movie you would like to watch: ")

user_request = user_request.strip()  # Remove any leading/trailing whitespace
user_request = user_request.lower()  # Convert to lowercase for consistency

movie_schedule = {movie.lower(): time for movie, time in movie_schedule.items()}  # Normalize keys to lowercase

if user_request in movie_schedule:
    print(f"The movie {user_request} is showing at {movie_schedule[user_request]}.")
else:
    print("Sorry, that movie is not in our schedule.")

