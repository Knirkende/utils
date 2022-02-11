import requests
import pprint
from SPARQLWrapper import SPARQLWrapper, JSON

def dbp_import_query():
    with open('query.rq', 'r') as file:
        query = file.read()
    sparql = SPARQLWrapper('http://dbpedia.org/sparql')
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

if __name__ == '__main__':
    print(dbp_import_query())