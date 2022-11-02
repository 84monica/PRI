# PRI

# Run Docker
`docker run -p 8983:8983 meic_solr`
# Create Core
`docker exec <containerName> bin/solr create_core -c books`
# Delete Core
`docker exec <containerName> bin/solr delete -c books`
# Get Data
`curl -X POST -H 'Content-type:application/json' --data-binary final_books_dataset.json http://localhost:8983/solr/books/update?commit=true`
# Add Schema
`curl -X POST -H 'Content-type:application/json' --data-binary schema.json http://localhost:8983/solr/books/schema`

# Queries

# Returns Books in the Fictional Category with ratings above 4, published between 2000 and 2020, with prices up to 4€
# Only Prints title, authors, categories, rating, published_date and price (for easier vizualization)
`curl 'http://localhost:8983/solr/books/select?fl=title%2C%20authors%2C%20categories%2C%20rating%2C%20price%2C%20published_date%2C&fq=rating%3A%5B4%20TO%20*%5D%2C%20published_date%3A%5B2000%20TO%202020%5D%2C%20price%3A%5B*%20TO%204%5D&indent=true&q.op=AND&q=categories%3Afiction' -d 'omitHeader=true'`