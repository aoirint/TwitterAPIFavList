
import json

with open('out.json', 'r') as fp:
  js = fp.read()

data = json.loads(js)

for entry in data:
  print(entry)
  print(entry['text'])

