from datetime import date
import pandas as pd

months = { "Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}

def change_author(author):
    authors = []
    for x in author:
        authors.append("['" + x + "']")
    return authors

def fix_genres(cats):
    newCats = []
    for x in cats:
        if (x == "none"):
            newCats.append(float("NaN"))
        else:
            y = x.replace("&amp,", "&")
            newCats.append(y)

    return newCats

def change_genres(cats):
    newCats = []
    for x in cats:
        if (type(x) == float):
            newCats.append(x)
        else:
            categories = x.split(" , ")
            row = []
            for y in categories:
                row.append(y)
            newCats.append(row)

    return newCats

def change_date2(dates):
    newDates = []
    for x in dates:
        dateList = str(x).split("-", 1)
        if (len(dateList) < 2):
            newDates.append(float("NaN"))
            continue
        year = dateList[0]

        stringDate = year


        newDates.append(stringDate)

    return newDates

def change_date(dates):
    newDates = []
    for x in dates:
        dateList = x.split(" ", 1)
        if (len(dateList) < 2):
            newDates.append(float("NaN"))
            continue
        month = dateList[0]
        day, year = dateList[1].split(", ")

        stringDate = year


        newDates.append(stringDate)

    return newDates

def change_price(prices, currency):
    newPrices = []
    for i in range(len(prices)):
        if (currency[i] == "Free"):
            newPrices.append(0.0)
        else:
            newPrices.append(round(prices[i] * 0.27, 2))

    return newPrices


data1299 = pd.read_csv('datasets/google_books_1299.csv', sep=',')
dataset = pd.read_csv('datasets/google_books_dataset.csv', sep=',')

dataset = dataset.rename(columns={ 'pageCount' : 'page_count', 'averageRating' : 'rating', 'publishedDate' : 'published_date'})
data1299 = data1299.rename(columns={ 'author' : 'authors', 'generes' : 'categories' })


dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]
data1299 = data1299.loc[:, ~data1299.columns.str.contains('^Unnamed')]
data1299["language"] = data1299["language"].map({"English" : "en"})
data1299["authors"] = change_author(data1299["authors"])
data1299["categories"] = fix_genres(data1299["categories"])
data1299["categories"] = change_genres(data1299["categories"])
data1299["published_date"] = change_date(data1299["published_date"])
dataset["published_date"] = change_date2(dataset["published_date"])
data1299["price"] = change_price(data1299["price"], data1299["currency"])


finalset = pd.concat([dataset, data1299], axis=0)

#finalset.drop("published_date", axis=1, inplace=True)
#finalset.drop("ISBN", axis=1, inplace=True)

#print(data1299["currency"].value_counts())
#print(data1299["price"])
#print(dataset)
print(finalset)

finalset.to_csv('final_books_dataset.csv')