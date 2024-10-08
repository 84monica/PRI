# Queries

* Returns Books in the Fictional Category with ratings above 4, published between 2000 and 2020, with prices up to 4€. Only Prints title, authors, categories, rating, published_date and price (for easier vizualization)
* `curl 'http://localhost:8983/solr/books/select?fl=title%2C%20authors%2C%20categories%2C%20rating%2C%20price%2C%20published_date%2C&fq=rating%3A%5B4%20TO%20*%5D%2C%20published_date%3A%5B2000%20TO%202020%5D%2C%20price%3A%5B*%20TO%204%5D&indent=true&q.op=AND&q=categories%3Afiction' -d 'omitHeader=true'`


* Returns Books of Fantasy about dragons ordered by highest rating. Only Prints title, authors, rating, published_date and description
* `curl 'http://localhost:8983/solr/books/select?fl=title%2C%20authors%2C%20rating%2C%20published_date%2C%20description&indent=true&q.op=OR&q=description%3A%22dragons%22%0Atitle%3A%22dragons%22%0Acategories%3A%22fantasy%22&rows=25&sort=rating%20desc' -d 'omitHeader=true'`


* Returns Books about Engineering from cheapest to more expensive and also ordered by highest rating. Only Prints title, language, categories, price, page_count and ISBN
* `curl 'http://localhost:8983/solr/books/select?fl=title%2C%20language%2C%20categories%2C%20price%2C%20page_count%2C%20ISBN&fq=price%3A%5B0%20TO%20*%5D&indent=true&q.op=OR&q=categories%3A%22Engineering%22%0Adescription%3A%22Engineering%22&rows=101&sort=rating%20desc%2C%20price%20asc' -d 'omitHeader=true'`

* Returns Books Comic Books. Only Prints title, authors, categories, published_date, price
* `curl 'http://localhost:8983/solr/books/select?fl=title%2C%20authors%2C%20published_date%2C%20categories%2C%20price&indent=true&q.op=OR&q=categories%3Acomics' -d 'omitHeader=true'`

* Returns Books about Murder in the Mystery Category. Only title, authors, categories, rating, page_count, price and description
* `curl 'http://localhost:8983/solr/books/select?fl=title%2C%20authors%2C%20categories%2C%20rating%2C%20page_count%2C%20price%2C%20description&indent=true&q.op=AND&q=description%3A%20murder%20%0Acategories%3Amystery&rows=12' -d 'omitHeader=true'`

* Returns Books about World Press. Only title, authors, description, price. Proximity Search
* `curl 'http://localhost:8983/solr/books/select?fl=title%2C%20ISBN%2C%20description%2C%20price%2C%20authors&indent=true&q.op=OR&q=description%3A%20%22must%20read%22~2&rows=33' -d 'omitHeader=true'`

* Retuns Books about sin, sun or son or that have *man in the title. Only title, authors, categories, ISBN,description, rating. Uses wildcard
* `curl 'http://localhost:8983/solr/books/select?fl=title%2C%20ISBN%2C%20categories%2C%20rating%2C%20description%2C%20authors&indent=true&q.op=OR&q=title%3A%20*man%0Adescription%3A%20s%3Fn&rows=61' -d 'omitHeader=true'`

* Returns Books writed by a Tom, a Tim or a team. Only title, authors, price, ISBN, description. Uses fuzzy search
* `curl 'http://localhost:8983/solr/books/select?fl=title%2C%20authors%2C%20price%2C%20ISBN%2C%20description&indent=true&q.op=OR&q=authors%3A%20tam~1&rows=29&start=0' -d 'omitHeader=true'`
