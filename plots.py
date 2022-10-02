from copy import copy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv('datasets/google_books_1299.csv')
print(dataset)

# AUTHORS
authors_count = dataset.groupby(dataset["author"]).count()["ISBN"].sort_values(ascending=False).head(11)

# configure plot
plt.rcParams.update({"font.size": 18})
plt.ylabel("Books Published")
plt.title("Authors")

# create plot
authors_count.plot.bar()
plt.xticks(rotation=45)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 16.5)
fig.savefig('images/authors_count.png')
plt.clf()

# RATINGS
ratings_count = dataset.groupby(dataset["rating"]).count()["ISBN"]

# configure plot
plt.rcParams.update({"font.size": 20})
plt.ylabel("Number of Books")
plt.title("Ratings")

# create plot
ratings_count.plot.bar()
plt.xticks(rotation=45)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 16.5)
fig.savefig('images/ratings.png')
plt.clf()

# GENRES
book_genres = dataset.groupby(dataset["generes"]).count()["ISBN"]
genre_dict = {}

# seperate genres
for (genres, num_movies) in book_genres.iteritems():
    genres_list_tmp = genres.split(" , ")
    genres_list = []
    for genre in genres_list_tmp:
        genres_list.extend(genre.split(" &amp, "))
    for genre in genres_list:
        if genre in genre_dict:
            genre_dict[genre] += num_movies
        else:
            genre_dict[genre] = num_movies

# sort by most common genres
genre_dict = {key: val for key, val in sorted(genre_dict.items(), key = lambda ele: ele[1], reverse = True)}

movies_genre_serie = pd.Series(genre_dict).head(12)

# configure plot
plt.rcParams.update({"font.size": 20})
plt.ylabel("Number of Books")
plt.title("Genres")

# create plot
movies_genre_serie.plot.bar()
plt.xticks(rotation=45)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 16.5)
fig.savefig('images/genres.png')
plt.clf()