# Tweetpy

## Abstract

Tweetpy is a software developed in Python for the automatic extraction from Twitter of posts containing a maximum of 5 hashtags relating to a single user profile. 
The information extracted is:  
description: the text of the tweet with the related hashtags on the topic
likes: number of likes that particular tweet has received 
retweets: how many times that tweet has been shared by other users
date: the day the tweet was published.

Tweetpy extracts all hashtags within a time frame allowed by Twitter. As an example, the extraction of hashtags relating to Coronavirus is used, for example: #Covid, # Covid-19, #Coronavirus, #pandemic and #swabs.

  ## System requirements

- python 3


Package Name|Link|License|Version
--------|--------|--------|--------
  tweepy  |  https://pypi.org/project/tweepy/ | MIT License | 3.9.0
  time  |  https://pypi.org/project/python-time/  | MIT License | 0.1.2
  csv |  https : //pypi.org/project/python-csv/  | MIT License | 0.0.13
  argparse  |  https://pypi.org/project/argparse/  |  Python Software Foundation License | 1.4.0
  datatime  |  https://pypi.org/project/DateTime /  | Zope Public License | 4.3
  writer  |  https://pypi.org/project/Writer/  | MIT License | 0.1.4
  crontab |  https://pypi.org/project/python-crontab/  | GNU Lesser General Public License  | 2.5.1

## Software description
### 4.1 The goal

The goal of Tweetpy is the extraction of tweets related to a given user profile, containing a maximum of 5 hashtags and dating back to the day before the current one. By launching Tweetpy once a day it is possible to retrieve the data daily and store it on a csv file for later analysis.
The software was developed in Python and is capable of extracting different data.
The example treated focuses on the extraction of news regarding the Coronavirus from a well-known information agency: Agenzia Ansa on Twitter. The keywords have been identified: Covid, Covid-19, Coronavirus, pandemic and swabs preceded by the hashtag (#Covid, # Covid-19, #Coronavirus, #pandemic and # swabs). 
The data are extracted from pages on Twitter chosen by the user. 
The information extracted is the following: 
description: it presents a brief description of the news with the relative link. 
likes: the number of likes that particular post has received 
retweets: the number of times that particular post has been shared by different users
date: the publication date of the post.

### 4.2 Components
The components that are part of the project are the following: 

- Twitter application: it is an application released by Twitter that makes credentials available to access the information contained on Twitter. The credentials are saved in a file called “credeniali.py”. 
- User Profile: The user identifies a profile whose information contained in the tweets is to be downloaded. 
- `tweetpy.py`: python file, which performs data extraction: description of the tweet, number of likes received on that particular tweet, number of retweets and the date and time when that tweet was published. “Tweetpy.py” receives in input the credentials plus the configuration from the user with respect to the information and outputs a .csv file containing the requested information. 
`- execute.sh`: executable file sh, is a script that periodically updates the .csv file through the crontab file. 


As input, Tweetpy takes the file“ credentials.py ”to access the information available on Twitter. As final output, Tweetpy produces a file in CSV format, named `data.csv`, containing the data extracted through“ tweetpy.py ”: description, number of likes, number of retweets and date.

The following figure shows the structure and relationship between the scripts to help the user in reading the Tweetpy architecture. 


![Components project](/home/giulia/Immagini/archittetura)





