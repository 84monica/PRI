import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv('datasets/google_books_1299.csv')

# PLOT AUTHORS WITH MOST BOOKS PUBLISHED
# create serie to plot
authors_count = dataset.groupby(dataset["author"]).count()["ISBN"].sort_values(ascending=False).head(10)

print(authors_count)

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

