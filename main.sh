#!/usr/bin/zsh
# Make the html_download.sh and main.sh executable
# chmod +x html_download.sh && chmod +x main.sh
# Usage:./main.sh <url> 

if [ -z "$1" ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

url=$1

python FUZZ_check.py $url
sleep(15) # giving time to complete the fuzz check
./html_download.sh
sleep(15) # giving time to completely download the html page
python data_scrap.py # calling the scrap program to scrap the data