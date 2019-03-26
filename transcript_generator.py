import argparse
import os
import sys
import requests

BASE_URL = 'https://video.google.com/timedtext'

def get_transcript(lang, vid):
    response = requests.get('{}/{}?{}'.format(lang, vid))
    print(response)

if __name__ == "__main__":
    # do some stuff with argparse
    parser = argparse.ArgumentParser(description='Generates a text file from youtube transcript api')
    parser.add_argument('lang', type=str, help='language')
    parser.add_argument('vid', type=str, help='video id')
    args = parser.parse_args()

    vid = args.vid
    lang = args.lang
    print(args)
    get_transcript(lang, vid)
    