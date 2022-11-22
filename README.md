# PRI

# HOW TO RUN

# Run Docker
`docker run -p 8983:8983 meic_solr`
# Create Core
`docker exec <containerName> bin/solr create_core -c books`
# Delete Core
`docker exec <containerName> bin/solr delete -c books`
# Run Python Scrip
`upload_data_and_schema.py`
# Run Frontend
`frontend.py`