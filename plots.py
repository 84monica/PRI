from copy import copy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv('datasets/google_books_1299.csv')
print(dataset)

# PLOT AUTHORS WITH MOST BOOKS PUBLISHED
authors_count = dataset.groupby(dataset["author"]).count()["ISBN"].sort_values(ascending=False).head(10)

# configure plot
plt.rcParams.update({"font.size": 8})
plt.ylabel("Books Published")
plt.title("Authors with the most Books Published")

# create plot
authors_count.plot.bar()

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('images/authors_count.png')
plt.clf()

# RATINGS
tmp_dataset = copy(dataset)
tmp_dataset["rating"] = round(tmp_dataset["rating"])

ratings_count = tmp_dataset.groupby(tmp_dataset["rating"]).count()["ISBN"]

# configure plot
plt.rcParams.update({"font.size": 8})
plt.ylabel("Number of Books")
plt.title("Ratings")

# create plot
ratings_count.plot.bar()

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('images/ratings.png')
plt.clf()