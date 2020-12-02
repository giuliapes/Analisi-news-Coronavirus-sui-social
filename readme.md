# Tweetpy

Software sviluppato in Python3 per l'estrazione automatica dei dati da Twitter. L'applicazione si concentra sull'estrazione di informazioni riguardanti il coronavirus da una nota agenzia di notizie su Twitter. Le informazioni estratte sono: descrizione della notizia, il numero di likes, il numero di retweets e la data del post stesso.

## Requisiti

* è richiesto l'utilizzo di python3.
* è richiesta la creazione e l'approvazione da parte di Twitter dell'App for developer, per poter ricevere le credenziali per l'estrazione dei dati.
* Sono richiesti i seguenti moduli, da installare mediante pip3:
- tweepy: https://pypi.org/project/tweepy/
- time: https://pypi.org/project/python-time/
- csv: https://pypi.org/project/python-csv/
- argparse: https://pypi.org/project/argparse/
- datatime: https://pypi.org/project/DateTime/
- writer: https://pypi.org/project/Writer/
- crontab: https://pypi.org/project/python-crontab/

## Struttura del progetto

- `credenziali.py` : file python, dove sono contenute le credenziali dell'App di Twitter per poter accedere alle informazioni che si vogliono estrarre.
- `tweetpyFinal.py` : file python, che esegue l'estrazione di dati: descrizione del tweet, numero di likes ricevuti su quel determinato tweet, numero di retweets e la data e orario in cui quel tweet è stato pubblicato.
- `execute.sh` : file eseguibile shell, è uno script programmato che contiene i comandi per eseguire il programma a una determinato ora e giorno impostato attraverso crontab
- `dati.csv`: file csv contenente i dati estratti attraverso tweetpyFinal: descrizione, numero di likes, numero di retweets e la data.

## Utilizzo

* Creare un account su https://developer.twitter.com/en, creare un'app compilando i campi richiesti come: lo scopo di utilizzo dell'App ecc....
* Ottenuta l'autorizzazione, accedere al portale per programmatori: https://developer.twitter.com/en/portal/dashboard e su dashboard nella sezione Project app selezionare l'icona con la chiave. Memorizzare le chiavi contenute nella sezione :API key & secret e Access token & secret.
* sul file `credenziali.py` salvare le credenziali memorizzate precedentemente attraverso delle variabili, chiamate: TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN e TWITTER_ACCESS_TOKEN_SECRET.
* eseguire il file `tweetpyFinal.py`, passando gli argomenti da linea di comando.
* in alternativa impostare il crontab in modo che l'estrazione dei dati avvenga in automatico impostando una determinata ora. Le informazioni per impostare il crontab: https://alvinalexander.com/linux/linux-crontab-file-format-example/.
* il file `execute.sh` eseguirà il file `tweetpyFinal.py`.
* i risultati verranno memorizzati nel file `dati.csv`.

### Argomenti utilizzati:

	- h1 seguito dall #Covid Obbligatorio
	- h2 seguito dall #Covid-19 Facoltativo
	- h3 seguito da #tamponi  Facoltativo
	- h4 seguito dall'#Pandemia Facoltativo
	- h5 seguito dall'#Coronavirus Facoltativo
	- UI seguito da Agenzia_Ansa Obbligatorio

### Esempio:

`` `
$ python3 tweetpyFinal.py -h1 "#covid" -h2 "#Covid-19" -h3 "#Coronavirus" -h4 "#tamponi" -h5 "#pandemia" -UI "Agenzia_Ansa"
`` `
