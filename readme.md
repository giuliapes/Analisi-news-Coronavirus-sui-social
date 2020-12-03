# Tweetpy

Tweetpy è un Software sviluppato in Python3 per l'estrazione automatica dei dati da Twitter. L'applicazione estrae dati riguardanti la pandemia di Coronavirus da una nota agenzia di informazione multimediale: Agenzia Ansa su Twitter. Le informazioni estratte sono: descrizione della notizia, il numero di likes, il numero di retweets e la data del post stesso.

## Requisiti

* è richiesto l'utilizzo di python3.
* è richiesta la creazione e l'approvazione da parte di Twitter dell'App for developer.
* Sono richiesti i seguenti moduli, da installare mediante pip3:
	* tweepy: https://pypi.org/project/tweepy/
 	* time: https://pypi.org/project/python-time/
 	* csv: https://pypi.org/project/python-csv/
 	* argparse: https://pypi.org/project/argparse/
 	* datatime: https://pypi.org/project/DateTime/
	*  writer: https://pypi.org/project/Writer/
 	* crontab: https://pypi.org/project/python-crontab/

## Struttura del progetto

- `credenziali.py` : file python, dove sono contenute le credenziali dell'App di Twitter per poter accedere alle informazioni che si vogliono estrarre.
- `tweetpyFinal.py` : file python, che esegue l'estrazione di dati: descrizione del tweet, numero di likes ricevuti su quel determinato tweet, numero di retweets e la data e orario in cui quel tweet è stato pubblicato.
- `execute.sh` : file eseguibile sh, è uno script che contiene i comandi per eseguire il “tweetpyFinal.py”  in un determinato orario del giorno settato attraverso l’uso del comando crontab di linux. Se interessati a l’utilizzo di questo file è necessario impostare le parole chiavi di interesse direttamente all’interno del programma execute.sh.
- `dati.csv`: file csv contenente i dati estratti attraverso tweetpyFinal: descrizione, numero di likes, numero di retweets e la data.

## Utilizzo

* Creare un account su https://developer.twitter.com/en e creare un'App compilando,in lingua inglese, i campi richiesti:
	* Le informazioni generali: dove vivi, come vorresti chiamarti sull'App
	* La sezione "In your words": descrizione dello scopo della creazione dell'App di Twitter. Per gli studenti o i professori è necessario includere il nome della 		scuola, dell'insegnante e il numero del corso
	* La sezione "The specifics": 
		* Descrizione di come verranno utilizzati i dati di Twitter e qualsiasi tipo di analisi dei dati che si intende svolgere
		* Descrizione dell'utilizzo previsto delle funzionalità sopra citate
		* Elenco di tutte le entità governative a cui si itende fornire i contenuti di Twitter o informazioni derivate in questo caso d'uso

* Ottenuta l'autorizzazione, accedere al portale per programmatori: https://developer.twitter.com/en/portal/dashboard e su "Dashboard" nella sezione "Project App" selezionare l'icona con la chiave. Memorizzare le chiavi contenute nella sezione "API key & secret e Access token & secret"
* Salvare nel file `credenziali.py` le credenziali memorizzate precedentemente attraverso delle variabili, chiamate: TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN e TWITTER_ACCESS_TOKEN_SECRET
* Eseguire il file `tweetpyFinal.py`, passando gli argomenti da linea di comando (vedi esempio)
* In alternativa impostare il crontab in modo che l'estrazione dei dati avvenga in automatico a una determinata ora eseguendo il file execute.sh (accertandosi di inserire le parole chiavi all’interno del file) presente all’interno del progetto. Le informazioni per impostare il crontab: https://alvinalexander.com/linux/linux-crontab-file-format-example/
* I risultati verranno memorizzati nel file `dati.csv`

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
![Image](https://user-images.githubusercontent.com/27484575/100906283-4f64a980-34c9-11eb-9a5c-038bc277863c.jpeg)

