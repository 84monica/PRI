import pandas as pd

data1299 = pd.read_csv('datasets/google_books_1299.csv', sep=',')
dataset = pd.read_csv('datasets/google_books_dataset.csv', sep=',')

dataset = dataset.rename(columns={ 'categories' : 'generes', 'pageCount' : 'page_count', 'averageRating' : 'rating', 'publishedDate' : 'published_data'})
data1299 = data1299.rename(columns={ 'author' : 'authors'})


dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]
data1299 = data1299.loc[:, ~data1299.columns.str.contains('^Unnamed')]


finalset = pd.concat([dataset, data1299], axis=0)


print(data1299)
print(dataset)
print(finalset)

finalset.to_csv('final_books_dataset.csv')