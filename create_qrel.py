import pandas as pd

isbn = pd.read_csv('final_books_dataset.csv')
isbn['price'] = isbn['price'].fillna(5.0)
isbn['rating'] = isbn['rating'].fillna(3.0)
isbn['price'] = pd.to_numeric(isbn['price'])
isbn['rating'] = pd.to_numeric(isbn['rating'])
isbn['published_date'] = pd.to_numeric(isbn['published_date'])

df_after_query = isbn.query("`rating` >= 4.0 and `price` <= 4.0 and `price` >= 0.0 and `published_date` <= 2020 and `published_date` >= 2000")
df_other_query = isbn.query("title.str.contains('Engineering') or categories.str.contains('Engineering') or description.str.contains('Engineering') and `price` >= 0.0", engine="python")
df_other_query = df_other_query.sort_values(by=['price', 'rating', 'title'], ascending=[True, False, False])
df_another_one = isbn.query("categories.str.contains('Fantasy') or title.str.contains('dragon') or description.str.contains('dragon') or categories.str.contains('Dragon')", engine="python")
df_another_one = df_another_one.sort_values(by=['rating', 'title'], ascending=[False, True])
df_comics = isbn.query("categories.str.contains('Comics', na=False)", engine="python")
df_mental_help = isbn.query("categories.str.contains('Mystery') and (title.str.contains('Murder') or description.str.contains('Murder'))", engine="python")
df_mental_help = df_mental_help.sort_values(by=["page_count"], ascending=[True])


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

f.close()

f = open('evaluation/q3rels.txt', 'w')

for x in df_other_query['title']:
    f.write(x + "\n")

f.close()

f = open('evaluation/q4rels.txt', 'w')

for x in df_comics['title']:
    f.write(x + "\n")

f.close()

f = open('evaluation/q5rels.txt', 'w')

for x in df_mental_help['title']:
    f.write(x + "\n")

f.close()
