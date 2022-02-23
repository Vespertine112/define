import json
import requests
import sys
import pyinputplus as pyip

__author__ = "Brayden Hill"
__email__ = "hillbgh@gmail.com"

api_url_init = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def main():
    search_string = ""
    if len(sys.argv) > 1:
        search_string = "+".join(sys.argv[1:])
    else:
        while search_string == "":
            search_string = pyip.inputStr("Please enter a search query:")
    
    req = requests.get(api_url_init + search_string)
    try:
        req.raise_for_status()
    except:
        print("\nError, word not found")
        sys.exit(1)
    


    if  req.json() is not None:
        print("\n")
        for entry in req.json():
            for meaning in entry["meanings"]:
                for defnitions in meaning["definitions"][:1]:
                        text = defnitions["definition"]
                        print(f"> {text}")
    else:
        print("No definition found")
        pass

if __name__ == '__main__':
    main()