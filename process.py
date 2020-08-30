from zd_article1 import data
import string

tags = set()

string.

def getTag(body, idx):
  tag = ''
  if body[idx] not in string.ascii_letters:
    print(f'debug {body[idx]}')
  while body[idx] in string.ascii_letters:
    tag += body[idx]
    idx += 1
  
  return tag

def getTags(body):
  gtags = set()
  for i, x in enumerate(body):
    if x == '<':
      if body[i+1] not in ['/', '!']:
        gtags.add(getTag(body, i+1))
  return gtags

for art in data['articles']:
  body = art['body']
  tags.update(getTags(body))

from pprint import pprint as pp

pp(tags)