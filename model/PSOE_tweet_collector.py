
from model.elasticsearch_utils import ElasticSearchCollector
from elasticsearch_dsl.query import Match, MatchAll, Wildcard
from model.tweet import Tweet
from collections import namedtuple
import json
from time import sleep


def collect_tweets(out_file_path):
    '''
    Este método ejecuta una secuencia de queries sobre la base de datos
    elasticsearch y guarda los resultados en el fichero cuyo nombre se
    indica como parámetro.
    '''
    collector = ElasticSearchCollector()

    # Refinar las queries anteriores (damos un hint a elasticsearch para que
    # nos de tweets con urls en el cuerpo del mensaje)
    url_query = Wildcard(**{'body.es': 'http*'})


    # Una query para cada candidato.
    queries = {
        'sanchez' : Match(**{'body.es' : '@sanchezcastejon'}) + url_query,
        'patxi' : Match(**{'body.es' : '@patxilopez'}) + url_query,
        'susana' : Match(**{'body.es' : '@susanadiaz'}) + url_query
    }



    # Hacemos las queries y páginamos los resultados.

    tweet_offset = 0
    num_tweets = 100 # Número de tweets por request
    while True:
        for candidate, query in queries.items():
            tweets = collector.search_tweets(query, first_tweet=tweet_offset, num_tweets = num_tweets)
            for tweet in tweets:
                tweet['candidate'] = candidate
                tweet['sources'] = tweet.get_info_sources()
                if len(tweet['sources']) == 0:
                    continue
                with open(out_file_path, 'a') as tweet_file_handler:
                    print(json.dumps(tweet), file = tweet_file_handler)

        tweet_offset += num_tweets


if __name__ == '__main__':
    collect_tweets('../data/tweets.json')
