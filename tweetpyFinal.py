#!/usr/bin/python3
from credenziali import * #importazione del file contenente le credenziali
import tweepy
import time
import csv
import argparse
import datetime
from csv import writer

# definisco gli args
parser = argparse.ArgumentParser()
parser.add_argument('-h1',type=str,required=True,help='selezione del primo hashtag es:#covid')
parser.add_argument('-h2',type=str,required=False,help='selezione del secondo hashtag es:#Covid-19')
parser.add_argument('-h3',type=str,required=False,help='selezione del primo hashtag es:#Coronavirus')
parser.add_argument('-h4',type=str,required=False,help='selezione del primo hashtag es:#tamponi')
parser.add_argument('-h5',type=str,required=False,help='selezione del primo hashtag es:#Pandemia')
parser.add_argument('-UI',type=str,required=True,help='sito es:Agenzia_Ansa')

args=parser.parse_args()

# controlli sugli argomenti passati da terminale per non obbligare l'utente ad utilizzargli tutti
# necessari per il corretto inserimento nella query di ricerca alla riga
if(args.h2==None):
    ar2 = ''
else:
    ar2 = args.h2
if(args.h3==None):
    ar3 = ''
else:
    ar3 = args.h3
if(args.h4==None):
    ar4 = ''
else:
    ar4 = args.h4
if(args.h5==None):
    ar5 = ''
else:
    ar5 = args.h5

# funzione per inserire in coda al file csv una lista di elementi
def appendiInCsv(file_name, list_of_elem):
    # Apro il file in modalità append, in modo che si possa scrivere in coda al contenuto del file
    with open(file_name, 'a+', newline='') as write_obj:
        #  Crea un oggetto writer dal modulo csv
        csv_writer = writer(write_obj,delimiter=';')
        # Aggiungi il contenuto dell'elenco come ultima riga nel file csv
        csv_writer.writerow(list_of_elem)

# legge le credenziali salvate nel file credenziali
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# list_csv = ["descrizione", "likes", "retweets", "data"]
# ["descrizione", "likes", "retweets", "data"] # usare solo per la creazione del file csv, poi eliminare
# appendiInCsv('dati.csv',list_csv)

# attraverso il modulo datetime ricavo il giorno odierno
today = datetime.date.today()
# creo una variabile one_day che vale 1 giorno
one_day = datetime.timedelta(days=1)
# creo una variabile yesterday per estrarre i dati del giorno precedente all'esecuzione del software
yesterday= (today-one_day)
# attraverso api.search seleziono i dati che voglio ricavare e la data dei dati che si vuole estrarre
for status in tweepy.Cursor(api.search, q="from:" + args.UI+" "+ args.h1 + " OR " + ar2 +" OR "+ ar3+ " OR "+ ar4 +" OR "+ ar5 + " since:" + str(yesterday)+ " until:" + str(today),tweet_mode='extended', lang='it').items():
    # appendo richiamando la funzione appendiInCsv: il testo della descrizione, il numero di likes, il numero di retweets e la data (nel formato yyyy-mm-dd oo:mm)
    appendiInCsv('ttt.csv',[status._json["full_text"], str(status.favorite_count), str(status.retweet_count), str(status.created_at)])
