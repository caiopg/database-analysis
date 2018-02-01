# Database analyzer
This repository is the source code for a program that queries a database provided by Udacity and outputs the result of the query.

## Preparing the environment
1. Install VirtualBox.
2. Install Vagrant.
3. Clone https://github.com/udacity/fullstack-nanodegree-vm
4. Using terminal, move to directory called vagrant found in the cloned repository.
5. Run command ```vagrant up```.
6. Download newsdata.sql from Udacity Project information.
7. Save newsdata.sql in vagrant directory in cloned repository.
8. Run command ```vagrant ssh``` from vagrant folder inside the cloned repository.
9. Move to /vagrant in virtual machine.
10. Run command ```psql -d news -f newsdata.sql``` in /vagrant.

## Creating necessay views in database
1. Using terminal, move to directory called vagrant found in the cloned repository.
2. Run command ```vagrant ssh``` from vagrant folder inside the cloned repository.
3. Move to /vagrant in virtual machine.
4. Run command ```psql news```.
1. Run the following commands:

```create view top_three_articles as select articles.title, count(log.path) as views from articles join log on (log.path like '%' || articles.slug) where log.status like '200%' group by articles.title order by views desc limit 3;```

```create view top_authors as select authors.name, views from authors join (select articles.author, count(log.path) as views from log join articles on (log.path like '%' || articles.slug) where log.status like '2%' group by articles.author order by views desc) as author_id_view_count on authors.id = author_id_view_count.author;```

```create view more_one_percent_requests_failed as select failed_requests.date, round((failed_requests.requests/total_requests.requests)*100,2) as percentage from (select date(log.time), cast(count(log.path) as numeric) as requests from log where log.status not like '2%' group by date(log.time)) as failed_requests join (select date(log.time), cast(count(log.path) as numeric) as requests from log group by date(log.time)) as total_requests on (failed_requests.date = total_requests.date) where (failed_requests.requests/total_requests.requests)*100 > 1;```

## Usage
1. Using terminal, move to directory called vagrant found in the cloned repository.
2. Run command ```vagrant ssh``` from vagrant folder inside the cloned repository.
3. Move to /vagrant in virtual machine.
4. Run ```python3 databaseanalyzerui.py```.
5. Follow instructions that appear in terminal.

