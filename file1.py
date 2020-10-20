from credenziali import *
import tweepy
import csv

print(tweepy.__version__)
userID = "Agenzia_ANSA"

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

'''tweets = api.user_timeline(screen_name=userID,
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )'''
#resultss = [status._json["full_text"] for status in tweepy.Cursor(api.search, q="from:Agenzia_Ansa #covid OR #Covid-19  OR #Coronavirus", tweet_mode='extended', lang='it').items()]
#like = [status.favorite_count for status in tweepy.Cursor(api.search, q="from:Agenzia_Ansa #covid OR #Covid-19  OR #Coronavirus", tweet_mode='extended', lang='it').items()]



'''results = []
likes = []
retweets = []
#quote_reply = []

for status in tweepy.Cursor(api.search, q="from:Agenzia_Ansa #covid OR #Covid-19  OR #Coronavirus", tweet_mode='extended', lang='it').items():
    results.append(status._json["full_text"])
    likes.append(status.favorite_count)
    retweets.append(status.retweet_count)
    #quote_reply.append(status.quote_count)
    print(status._json["full_text"] , ' ',status.favorite_count, ' ' , status.retweet_count, ' ')

print(len(results))
print(len(likes))
print(len(retweets))'''

list_csv = [["descrizione", "likes", "retweets"]]
for status in tweepy.Cursor(api.search, q="from:Agenzia_Ansa #covid OR #Covid-19  OR #Coronavirus", tweet_mode='extended', lang='it').items():
    list_csv.append([status._json["full_text"], str(status.favorite_count), str(status.retweet_count)])

with open('twitter.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(list_csv)

#print(list_csv[0:2])



#print(len(quote_reply))

#my_tweets = []
'''for result in resultss:
    if not "@Agenzia_Ansa" in result:
        print(result+ '\n')'''
#print(len(resultss))
#print(len(like))

#print(len(results))
#print(len(likes))

    #my_tweets.append(result["full_text"])
    #print(result["full_text"])

#all_tweets = []
#all_tweets.extend(tweets)
#oldest_id = tweets[-1].id
