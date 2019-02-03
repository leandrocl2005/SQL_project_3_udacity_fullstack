#!/usr/bin/env python3
import psycopg2


def get_query_result(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def print_breaks():
    print()
    print("########==============================================########")
    print()


query = """
SELECT title_path.t, count(log.path) AS c
FROM
    (SELECT DISTINCT
        articles.title AS t,
        log.path AS p
    FROM
        articles
    LEFT JOIN log
    ON log.path ILIKE '%' || articles.slug || '%'
    AND log.status = '200 OK') AS title_path
LEFT JOIN log on log.path = title_path.p
GROUP BY title_path.t
ORDER BY c DESC
LIMIT(3);
"""

print("Quais são os três artigos mais populares de todos os tempos?")
print()
print("{:>35s}{:>20s}".format("Título", "Nº de acessos"))
for row in get_query_result(query):
    print("{:>35s}{:>20d}".format(row[0], row[1]))
print_breaks()

query = """
SELECT slug_name.aun, count(log.path) AS c
FROM
    (SELECT
        articles.slug AS ars,
        authors.name AS aun
    FROM
        authors
    LEFT JOIN articles
    ON authors.id = articles.author) AS slug_name
LEFT JOIN log
ON log.path ILIKE '%' || slug_name.ars || '%'
AND log.status = '200 OK'
GROUP BY slug_name.aun
ORDER BY c DESC
LIMIT(3);
"""

print("Quem são os autores de artigos mais populares de todos os tempos?")
print()
print("{:>35s}{:>20s}".format("Author", "Nº de acessos"))
for row in get_query_result(query):
    print("{:>35s}{:>20d}".format(row[0], row[1]))
print_breaks()

query = """
SELECT *
FROM
    (SELECT
        to_char(date_trunc('day', time), 'DD Mon YYYY'),
        (SUM(
            CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END
        )::DECIMAL / COUNT(status) ) * 100 AS percent_total
    FROM log
    GROUP BY 1
    ORDER BY 1) AS temp_table
WHERE percent_total > 1;
"""

print("Em quais dias mais de 1% das requisições resultaram em erros?")
print()
print("{:>15s}{:>20s}".format("DATA", "PORCENTAGEM (%)"))
result = get_query_result(query)[0]
print("{:>15s}{:>19.4f}%".format(result[0], float(result[1])))
print_breaks()
