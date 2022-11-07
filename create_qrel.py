import pandas as pd

isbn = pd.read_csv('final_books_dataset.csv')
isbn['price'] = isbn['price'].fillna(5.0)
isbn['rating'] = isbn['rating'].fillna(3.0)
isbn['price'] = pd.to_numeric(isbn['price'])
isbn['rating'] = pd.to_numeric(isbn['rating'])
isbn['published_date'] = pd.to_numeric(isbn['published_date'])

df_after_query = isbn.query("`rating` >= 4.0 and `price` <= 4.0 and `price` >= 0.0 and `published_date` <= 2020 and `published_date` >= 2000")
df_other_query = isbn.query("title.str.contains('Engineering') or categories.str.contains('Engineering')", engine="python")
df_other_query = df_other_query.sort_values(by=['price', 'rating'], ascending=[True, False])
df_another_one = isbn.query("categories.str.contains('Fantasy') and (title.str.contains('dragon') or title.str.contains('Dragon') or description.str.contains('dragon') or description.str.contains('dragon'))", engine="python")
df_another_one = df_another_one.sort_values(by=['rating'], ascending=False)

titles = []

for index, row in df_after_query.iterrows():
    if type(row['categories']) is float:
        continue
    elif 'Fiction' in row['categories']:
        titles.append(row['title'])

f = open('evaluation/q1rels.txt', 'w')

for x in titles:
    f.write(x + "\n")

f.close()

f = open('evaluation/q2rels.txt', 'w')

for x in df_another_one['title']:
    f.write(x + "\n")

f.close

f = open('evaluation/q3rels.txt', 'w')

for x in df_other_query['title']:
    f.write(x + "\n")

f.close
