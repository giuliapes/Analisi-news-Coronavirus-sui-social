#!/usr/bin/python3

from credenziali import * #importazione del file contenente le credenziali
import tweepy
import time
import csv
import argparse
import datetime
from csv import writer

parser = argparse.ArgumentParser()
parser.add_argument('-h1',type=str,required=True,help='selezione del primo hashtag es:#covid')
parser.add_argument('-h2',type=str,required=False,help='selezione del secondo hashtag es:#Covid-19')
parser.add_argument('-h3',type=str,required=False,help='selezione del primo hashtag es:#Coronavirus')
parser.add_argument('-h4',type=str,required=False,help='selezione del primo hashtag es:#tamponi')
parser.add_argument('-h5',type=str,required=False,help='selezione del primo hashtag es:#Pandemia')
parser.add_argument('-UI',type=str,required=True,help='sito es:Agenzia_Ansa')

args=parser.parse_args()


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj,delimiter=',')
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

#userID = "Agenzia_ANSA"
#legge le credenziali salvate nel file credenziali
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#estrazione e salvataggio in csv di: descrizione dei tweet, n like e n di retweet
today = datetime.date.today()

# ["descrizione", "likes", "retweets", "data"] usare solo per la creazione del file csv poi eliminare da lista_csv
list_csv = ["descrizione", "likes", "retweets", "data"]
append_list_as_row('prd1.csv',list_csv)
today = datetime.date.today()
one_day = datetime.timedelta(days=1)
yesterday= (today-one_day)
for status in tweepy.Cursor(api.search, q="from:" + args.UI+" "+ args.h1 + " OR " + args.h2 +" OR "+ args.h3+ " OR "+ args.h4 +" OR "+ args.h5 + " since:" + str(yesterday)+ " until:" + str(today),tweet_mode='extended', lang='it').items():
    append_list_as_row('prd1.csv',[status._json["full_text"], str(status.favorite_count), str(status.retweet_count), str(status.created_at)])

#with open('prova1.csv', 'a', newline='') as file:
#    writer = csv.writer(file, delimiter=';')
#    writer.writerows(list_csv)
