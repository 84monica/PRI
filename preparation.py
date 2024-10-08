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

def change_date(dates):
    newDates = []
    for x in dates:
        dateList = x.split(" ", 1)
        if (len(dateList) < 2):
            newDates.append("")
            continue
        _, year = dateList[1].split(", ")
        if len(year) != 4:
            year = "" 

        if not(year.isnumeric()):
            year = ""

        newDates.append(year)

    return newDates

def change_date2(dates):
    newDates = []
    for x in dates:
        dateList = str(x).split("-", 1)
        year = dateList[0]
        if len(year) != 4:
            year = "" 

        if not(str(year).isnumeric()):
            year = ""

        newDates.append(year)

    return newDates

def fix_isbn(isbns):
    newIsbn = []
    for x in isbns:
        if x == "Original pages" or x == "Flowing text" or x == "Flowing text, Google-generated PDF":
            x=""
        if not(x.isnumeric()):
            x=""
        else:
            if not x.find(":") == -1:
                index = x.find(":")
                x = x[index+1:]
        newIsbn.append(x)

    return newIsbn

def change_price(prices, currency):
    newPrices = []
    for i in range(len(prices)):
        if (currency[i] == "Free"):
            newPrices.append(0.0)
        elif currency[i] == "EUR" or currency[i] == "Not for sale":
            newPrices.append(prices[i])
        else:
            newPrices.append(round(prices[i] * 0.27, 2))

    return newPrices


# data1299 = pd.read_csv('datasets/1299_complete.csv', sep=',')
# dataset = pd.read_csv('datasets/dataset_complete.csv', sep=',')
data1299 = pd.read_csv('datasets/dataset_intermidiate_1299.csv', sep=',')
dataset = pd.read_csv('datasets/dataset_intermidiate.csv', sep=',')

dataset = dataset.rename(columns={ 'pageCount' : 'page_count', 'averageRating' : 'rating', 'publishedDate' : 'published_date', 'isbn' : 'ISBN'})
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

dataset = dataset.drop_duplicates()

finalset = pd.concat([dataset, data1299], axis=0)
finalset["ISBN"] = fix_isbn(finalset["ISBN"])
finalset = finalset.drop_duplicates(subset="ISBN", keep="first")
print(finalset)

#finalset.to_csv('final.csv')
finalset.to_csv('final_books_dataset.csv')
