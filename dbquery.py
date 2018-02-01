import sys

import psycopg2


def top_three_articles():
    query = "select * from top_three_articles;"

    return do_query(query)


def top_authors():
    query = "select * from top_authors;"
    return do_query(query)


def more_one_percent_requests_failed():
    query = "select * from more_one_percent_requests_failed;"

    return do_query(query)


def do_query(query):
    try:
        db = psycopg2.connect("dbname=news")

        cursor = db.cursor()

        cursor.execute(query)
        result = cursor.fetchall()

        db.close()
        return result

    except psycopg2.Error:
        print("\n UNABLE TO CONNECT TO DATABASE\n")
        sys.exit(1)
