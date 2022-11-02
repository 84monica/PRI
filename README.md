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