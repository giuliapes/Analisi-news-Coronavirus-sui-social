from credenziali import * #importazione del file contenente le credenziali
import tweepy
import time
import csv
import xlsxwriter
import sys

print(tweepy.__version__)

userID = "Agenzia_ANSA"
#legge le credenziali salvate nel file credenziali
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#estrazione e salvataggio in csv di: descrizione dei tweet, n like e n di retweet

# ["descrizione", "likes", "retweets", "data"] usare solo per la creazione del file csv poi eliminare da lista_csv
list_csv = []
for status in tweepy.Cursor(api.search, q="from:Agenzia_Ansa #covid OR #Covid-19  OR #Coronavirus OR covid OR #tamponi OR #pandemia", tweet_mode='extended', lang='it').items():
    list_csv.append([status._json["full_text"], str(status.favorite_count), str(status.retweet_count), str(status.created_at)])


with open('dati.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(list_csv)

#sorted ("full_text")
