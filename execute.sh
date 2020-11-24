#! /bin/bash
echo "Script started..."

has1='-h1 #covid'
has2='-h2 #Covid-19'
has3='-h3 #tamponi'
has4='-h4 #Pandemia'
has5='-h5 #Coronavirus'
UI='-UI Agenzia_Ansa'
cd /home/giulia/Scrivania/Reazioni-news-Coronavirus-sui-social

/usr/bin/python3 tweetpyFinal.py $has1 $has2 $has3 $has4 $has5 $UI

echo "Script finished correctly"
