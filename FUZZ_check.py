# This program is to check all the valid webpage
# This program checks if the webpage give 200 status code if it does, saves the list to a file exist_url.txt

import requests
import time
import sys

def main(url):
    with open("FUZZ.txt","r") as fuzz:
        for fuzzs in fuzz:
            content = fuzzs.strip()
            check_url = f"{url}/{content}"
            responce = requests.get(check_url) # Getting the status code
            if responce.status_code == 200:
                # checking the response if 200 saves it to the file exsist_url.txt
                with open("exsist_url.txt","a") as exsist:
                    exsist.write(check_url + "\n")
                    time.sleep(2) # adding delay to not overload the server
            else:
                time.sleep(2)
    with open("exsist_url.txt","a") as exsist:
        # At the last adding the initial url itself
        exsist.write(url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <url>")
        sys.exit(1)    
    url = sys.argv[1]
    main(url)