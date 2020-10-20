from credenziali import * #importazione del file contenente le credenziali
import tweepy
import csv

print(tweepy.__version__)
userID = "Agenzia_ANSA"
#legge le credenziali salvate nel file credenziali
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#estrazione e salvataggio in csv di: descrizione dei tweet, n like e n di retweet
list_csv = [["descrizione", "likes", "retweets"]]
for status in tweepy.Cursor(api.search, q="from:Agenzia_Ansa #covid OR #Covid-19  OR #Coronavirus", tweet_mode='extended', lang='it').items():
    list_csv.append([status._json["full_text"], str(status.favorite_count), str(status.retweet_count)])

with open('twitter.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(list_csv)
