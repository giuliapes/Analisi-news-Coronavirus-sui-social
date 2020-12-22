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
  csv |  https://pypi.org/project/python-csv/   | MIT License | 0.0.13
  argparse  |  https://pypi.org/project/argparse/  |  Python Software Foundation License | 1.4.0
  datatime  |  https://pypi.org/project/DateTime/  | Zope Public License | 4.3
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


![Components project]('/home/giulia/Immagini/archittetura')

The figure above shows the software structure. On the one hand,  there is Twitter which contains the Twitter App that the user creates on twitter for the developer portal. These issues credentials, indicated with the name app TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET are saved in the “credentials.py” file. Within Twitter, there is also the user profile from which you wish to extrapolate the information contained in the tweets. An example would be that of any public user: tweet1, tweet2, ..., tweet n. Each tweet owns a certain type of hashtag, such as: tweet1 owns hashtag1 (# hash1), tweet2 owns hashtag1 and hashtag2 (# hash1 and # hash2) and tweet n owns hastag2 (# hash2). 
Tweetpy is used by a user ("User Profile") who specifies a user profile and the hashtag he/ she searches, executes the file "tweetpy.py" which takes as input the "credentials.py" file to access Twitter, and produces as output a file called “data.csv” with a table containing the various tweets with the specified hashtags. 
It is possible to make the automatic execution of the software using the execute.sh file which receives the same information, such as the specification of the user profile and the type of hashtag to search for. The execute.sh file is taken as input from a crontab file, which runs periodically and updates the data within the data.csv file.
## 4.3 License

Tweetpy is released under a General Public License, commonly referred to as GNU, which is a strongly copyleft license for free software. It is based on the freedom to use and share the Software according to your needs and the possibility of being able to make changes to the application itself. 
# Using the software
## 5.1 Installation

Clone the repository with the git clone command from the terminal: https://github.com/giuliapes/Tweetpy 

Create an account and the Twitter App for developer: https://developer.twitter.com/en 
Extracting data from the Twitter news and microblogging service requires a license to access the “App for developer” section. It is necessary to fill in the following fields: 
 
  - General information: where you live, how you would like to call yourself on the App
  - The "In your words" section: description of the purpose for creating the App. For students or professors it is necessary to include the name of the school, the teacher and the number of the course
  - The section "The specifics":
      * Description of how the Twitter data will be used and any type of analysis you intend to carry out
      * Description of use provided for the aforementioned functions
      * List of all government entities to which you intend to provide Twitter content or derived information in this use case

Once you have obtained the license on Twitter for the App, you access the "Dashboard" where, in the “Project App” section, you can find the necessary keys: “API key & secret” and “Access token & secret”. 

  --> Install the modules listed in System requirements using python pip3: example: pip3 install csv
  --> Create the "credentials.py" file by inserting your credentials issued by the App into the variables


## 5.2 Running the software

There are two ways of running the software: the manual and the automatic execution. 

### 5.2.1 The manual execution
The manual execution is performed by launching the tweetpy.py command, specifying the input data with the following parameters.

input:

Parameter|Description| |Exemple
--------|--------|--------|--------
  -h1  |  first hashtag to extract | Mandatory |-h1 "#Covid"
  -h2 | second hashtag to extract |  Not mandatory| -h2 "#Covid-19"
  -h3 |  third hashtag to extract  | Not mandatory | -h3 "#Coronavirus"
  -h4  |   fourth hashtag to be extracted | Not mandatory  | -h4 "#swabs"
  -h5  |  fifth hashtag to be extracted | Not mandatory| -h5 "#pandemic"
  -UI | username of the user profile whose hashtag you want to extract | Mandatory | -UI "Agenzia_Ansa"
  

As a result, the software extracts all the tweets related to the specified profile, containing the specified hashtags related to the day before the one when the script is launched. Consequently, the software produces the following output in csv format:


description|likes|retweets| date
--------|--------|--------|--------
 Contains the text of the tweet, it may contain additional hashtags beyond those specified, links to other users and the news link, which leads the user directly to the Agency website Ansa |  Contains the number of likes of other users in a given news | Contains the number of shares of a tweet. How many times that tweet has been shared by other users |Contains the date of publication of the tweet on the user profile
 

 Example of the manual execution:

<i> python tweetpy -h1 "#Covid" -h2 "# Covid-19" -h3 "#Coronavirus" -h4 “#pandemic” -h5 “#swabs” -UI “Agenzia_Ansa”</i>

Output:
description|likes|retweets|date
--------|--------|--------|--------
La #Scala, a unique first time of the #Covid. Stellar cast, scenography and the anthem sung by the workers #ANSA @teatroallascala https://t.co/lqP3I2uTGX |  14 | 4 |2020-12-06 08:50:02
#Covid-19 #Usa, over a million cases in 5 #ANSA days https://t.co/Y7MwDsYHkL |16| 10|2020-12-06 09:50:02
#Covid: 18,887 new cases and 564 victims in Italy in the last 24 hours #ANSA https://t.co/cYSbib309p| 31  | 9 | 2020-12-06 19:39:50

#Covid, #Abruzzo ordinance: from tomorrow out of the red zone. Marsilio: 'It turns orange, I informed Speranza'. But government sources: 'It has to wait for Wednesday. The deadline of 21 days must be respected. No endorsement of decision on tomorrow '#ANSA https://t.co/jBqnUixYth | 41 | 9 | 2020-12-06 21:30:28

#Covid: Abruzzo ordinance in force tomorrow, shops reopen. Sources Region: 'Valid measures, the Government can only challenge them'. Boccia: 'Abruzzo will be warned if orange from tomorrow' #ANSA https://t.co/6PA48XW7rM https://t.co/bEDKQ5ELb9| 71 | 41 | -2020-12-06 22:17:46

#Covid Bavaria declares a state of calamity , new restrictions 'We must do more'. Lockdown even more severe #ANSA https://t.co/nOucqM5M0p| 42 |11 |2020-12-06 22:32:33


### 5.2.2 The automatic execution

In this case, the execute.sh script is used, by taking the same input parameters as for the manual execution. Furthermore, the full path to the folder Tweetpy must also be specified.

Next, the crontab must be configured to periodically execute the execute.sh script. In this way, every day you can download the given user’s tweets of the previous day, which contain the specified hashtags.


Thanks to crontab, you can set up operations on the system with a certain simplicity using the "cron daemon". The latter reads the crontab file and executes the operations at the specified time. To specify the time and day when you want to run the file, you need to run from the command line:

 <i>crontab -e </i>

used to insert, modify or delete scheduled tasks. This will open the text editor where you will enter the scheduled task. 
Each operation must necessarily contain the time and day of execution. It is also possible to insert more operations. To do this, it is necessary to start a new line. An example of setting the time and date is the following: 

<i>00 00 * * * /usr/bin/execute.sh</i>

In the specified operation, the cron daemon was instructed to execute the execute.sh command, every day at minute 00 hour 00 (midnight).  
Before executing the command, you must enter in the order: minute, hour, day of the month, month, day of the week. 
The symbol * is used to indicate all values. If it is used on the day of the month, as in the previous example, the command will run every day.  

As final output, the script will produce the same output file as the tweetpy.py script, with the difference that the output file will be updated periodically.








