import argparse
import os
import sys
import requests
from xml.etree import ElementTree

BASE_URL = 'https://video.google.com/timedtext?lang='

def get_transcript(lang, vid):
    response = requests.get('{}{}&v={}'.format(BASE_URL, lang, vid))
    if response.status_code == 200:
        return ElementTree.fromstring(response.content)
    return None

if __name__ == "__main__":
    # do some stuff with argparse
    parser = argparse.ArgumentParser(description='Generates a text file from youtube transcript api')
    parser.add_argument('lang', type=str, help='language')
    parser.add_argument('vid', type=str, help='video id')
    args = parser.parse_args()

    vid = args.vid
    lang = args.lang

    transcript = get_transcript(lang, vid)


    sys.stdout.write("Retrieving video transcript...")
    print(transcript)
    sys.exit(0)
    