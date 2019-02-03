# Log analysis with postgres SQL and Python

In this project we'll build a data reporting on a postgres database with a log table using *Python 3.5.2* and *psycopg2* library.

## Installation of virtual-machine

First, we need to create our virtual machine with all settings for this project:

* Install Oracle VM VirtualBox
* Install Vagrant

Replace the *newsdata.sql* in *newsdata* folder by the *newsdata.sql* provide by Udacity in this link: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Enter with the commands in Git Bash:

```sh
$ git clone https://github.com/leandrocl2005/SQL_project_3_udacity_fullstack.git
$ cd SQL_project3_udacity_fullstack/
$ cd vagrant
$ vagrant up
$ vagrant ssh
```

If all things are right, we are in our VM!

## Creating the news database

Let's create our database:

```sh
$ cd ..
$ cd ..
$ cd vagrant
$ psql -d news -f newsdata/newsdata.sql
```

The dataset contains 3 tables: articles, authors and log. To see it, in Git Bash enter:

```sh
$ psql -d news
$ news => \dt
```

To exit from psql, just press Ctrl+D. 

## The analysis

We want to answer 3 questions about the tables in our database (the questions are in pt-br language):

* "Quais são os três artigos mais populares de todos os tempos?"
* "Quem são os autores de artigos mais populares de todos os tempos?"
* "Em quais dias mais de 1% das requisições resultaram em erros?"

To do that, just tip in Git Bash the following:

```sh
$ python3 main.py
```

The result is like *result.txt* file.

# Credits

  - the *news.sql* and the vagrant setup files were provided by Udacity


