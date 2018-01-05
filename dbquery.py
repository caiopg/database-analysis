import psycopg2


def top_three_articles():
    query = "select articles.title, count(log.path) as views from articles, " \
            "log where log.path like '%' || articles.slug and log.status " \
            "like '200%' group by articles.title order by views desc limit 3; "

    return do_query(query)


def top_authors():
    query = "select authors.name, author_id_view_count.views from authors, " \
            "author_id_view_count where authors.id = " \
            "author_id_view_count.author; "

    return do_query(query)


def more_one_percent_requests_failed():
    query = "select failed_requests.date, round((" \
            "failed_requests.requests/total_requests.requests)*100, " \
            "2) as percentage from failed_requests, total_requests where " \
            "failed_requests.date = total_requests.date and (" \
            "failed_requests.requests/total_requests.requests)*100  > 1; "

    return do_query(query)


def do_query(query):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    db.close()
    return result
