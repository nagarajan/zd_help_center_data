import json
import os
from html.parser import HTMLParser
from pprint import pp


tags = set()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tags.add(tag)

dataDir = 'data/en-us'
files = [
    'articles_1.json',
    'articles_2.json',
    'articles_3.json',
]


parser = MyHTMLParser()

for fn in files:
    data = json.loads(open(os.path.join(dataDir, fn)).read())
    for article in data['articles']:
        parser.feed(article['body'])

print(', '.join(sorted(tags)))

