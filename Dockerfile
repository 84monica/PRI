FROM solr:8.10

COPY final_books_dataset.json data/final_books_dataset.json

COPY schema.json /data/schema.json

COPY synonyms.txt /data/synonyms.txt

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
