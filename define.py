#!/usr/bin/env python
import json
import argparse
import requests
import sys
import pyinputplus as pyip

__author__ = "Brayden Hill"
__email__ = "hillbgh@gmail.com"

api_url_init = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def main():
    parser = argparse.ArgumentParser(description="A common word definition Tool")
    parser.add_argument(
        '-e',
        help="Include extraneous information"
    )
    args_space, word = parser.parse_known_args()
    
    if args_space.e != None:
        search_string = args_space.e
    else:
        search_string = "+".join(word)

    while word == None:
        search_string = pyip.inputStr("Please enter a search query:")
    
    req = requests.get(api_url_init + search_string)
    try:
        req.raise_for_status()
    except:
        print("\nError, word not found")
        sys.exit(1)
    
    if  req.json() is not None:
        for entry in req.json():
            for meaning in entry["meanings"]:
                part_o_speech = meaning["partOfSpeech"]
                for defnitions in meaning["definitions"][:1]:
                        text = defnitions["definition"]
                        try:
                            example = defnitions["example"]
                        except:
                            example = "No example provided"
                        if args_space.e == None:
                            print(f"{search_string} : {part_o_speech}\n > {text}")
                        else:
                            print(f"{search_string} : {part_o_speech}\n > {text}\nExample: {example}\n")

    else:
        print("No definition found")
        pass

if __name__ == '__main__':

    main()