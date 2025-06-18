# This program uses BeautifulSoup to extract the data
# BeatifulSoup is a python package that helps use to parse html and xml files
# This program extract the data from the downloaded html files and display it
# After that this deletes all the folder output_dir to save up space

from bs4 import BeautifulSoup
import os
import time
import shutil

i = 1
for files in os.listdir("output_dir"):
    with open(f"output_dir/{files}","r",encoding="utf-8") as file:
        doc = BeautifulSoup(file,"html.parser")

        print(f"Parsing {i} .")
        time.sleep(1)
        print(f"Parsing {i} ..")
        time.sleep(1)
        print(f"Parsing {i} ...")
        time.sleep(1)
        print(f"Parsing {i} ....")

        title = doc.title.string if doc.title else "No title found"
        print(f"\nTitle: {title}")

        # Meta tags
        for meta in doc.find_all("meta"):
            name = meta.get("name", "N/A")
            content = meta.get("content", "N/A")
            print(f"\t{name}: {content}")

        # CSS Links (note: tag name is 'link', not 'links')
        for link in doc.find_all("link", rel="stylesheet"):
            print(f"\tStylesheet: {link.get('href')}")

        # Hidden Inputs
        for hidden in doc.find_all("input", {"type": "hidden"}):
            print(f"\tHidden field - {hidden.get('name')}: {hidden.get('value')}")

        # Hyperlinks
        for anchor in doc.find_all("a", href=True):
            print(f"\tHyperlink: {anchor.get('href')}")

        i = i + 1

shutil.rmtree("output_dir") # Delete the output_dir directory 

if os.path("output_dir"):
    # Checking if deleted or not
    print("Directory removing failed")
else:
    print("Directory removing success")
