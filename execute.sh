#! /bin/bash
echo "Script started..."

has1='-h1 #covid'
has2='-h2 #Covid-19'
has3='-h3 #tamponi'
has4='-h4 #Pandemia'
has5='-h5 #Coronavirus'
UI='-UI Agenzia_Ansa'
# specificare il percorso alla cartella al posto di ...
cd .../Tweetpy
/usr/bin/python3 tweetpy.py $has1 $has2 $has3 $has4 $has5 $UI

echo "Script finished correctly"
