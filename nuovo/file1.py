from credenziali import * #importazione del file contenente le credenziali
import tweepy
import time
import csv
import xlsxwriter
import sys
import argparse
import datetime

print(tweepy.__version__)
parser = argparse.ArgumentParser()
parser.add_argument('-h1',type=str,required=True,help='selezione del primo hashtag es:#covid')
parser.add_argument('-h2',type=str,required=False,help='selezione del secondo hashtag es:#Covid-19')
parser.add_argument('-h3',type=str,required=False,help='selezione del primo hashtag es:#Coronavirus')
parser.add_argument('-h4',type=str,required=False,help='selezione del primo hashtag es:#tamponi')
parser.add_argument('-h5',type=str,required=False,help='selezione del primo hashtag es:#Pandemia')
parser.add_argument('-UI',type=str,required=True,help='sito es:Agenzia_Ansa')

args=parser.parse_args()
print(args.h1)

#userID = "Agenzia_ANSA"
#legge le credenziali salvate nel file credenziali
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#estrazione e salvataggio in csv di: descrizione dei tweet, n like e n di retweet
today = datetime.date.today()

# ["descrizione", "likes", "retweets", "data"] usare solo per la creazione del file csv poi eliminare da lista_csv
list_csv = []
for status in tweepy.Cursor(api.search, q="from:" + args.UI+" "+ args.h1 + " OR " + args.h2 +" OR "+ args.h3+ " OR "+args.h4+" OR "+ args.h5 + " since:" + str(today.year)+"-"+ str(today.month)+"-"+ str(today.day-1)+ " until:" + str(today.year)+"-"+ str(today.month)+"-"+ str(today.day),tweet_mode='extended', lang='it').items():
    list_csv.append([status._json["full_text"], str(status.favorite_count), str(status.retweet_count), str(status.created_at)])


with open('7.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(list_csv)
