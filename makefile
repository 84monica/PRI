all: preparation.csv

#Does some final dataset organizing and merges the two datasets
final.csv: 1299_complete.csv dataset_complete.csv
	python3 preparation.py

#Retrieves thumbnails from the Google Books API
1299_complete.csv: datasets/google_books_1299.csv
	python3 getThumbnails.py

#Simulates a manual filtering if nececssary
database_complete.csv: dataset_intermidiate.csv
	python3 simulateDatasetFilter.py

#Retrieves isbn,price,currency,descirption and thumbnails from the Google Books API
database_intermidiate.csv: datasets/google_books_dataset.csv
	python3 getDatasetData.py

clean:
	rm final.csv
	rm 1299_complete.csv
	rm database_complete.csv
	rm database_intermidiate.csv
