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

```create view author_id_view_count as select articles.author, count(log.path) as views from log, articles where log.path like '%' || articles.slug and log.status like '2%' group by articles.author order by views desc;```

```create view failed_requests as select date(log.time), cast(count(log.path) as numeric) as requests from log where log.status not like '2%' group by date(log.time);```

```create view total_requests as select date(log.time), cast(count(log.path) as numeric) as requests from log group by date(log.time);```

## Usage
1. Using terminal, move to directory called vagrant found in the cloned repository.
2. Run command ```vagrant ssh``` from vagrant folder inside the cloned repository.
3. Move to /vagrant in virtual machine.
4. Run ```python3 databaseanalyzerui.py```.
5. Follow instructions that appear in terminal.

