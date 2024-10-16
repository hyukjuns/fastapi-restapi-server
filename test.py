import json
import re

shapes = [
  {
    'shape': 'square',
    'width': 40,
    'height': 40
  },
  {
    'shape': 'rectangle',
    'width': 30,
    'height': 40

  }
]

print(enumerate(shapes))
for i, d in enumerate(shapes):
    print(i, d)

print(i) 

print(re.M)
if re.search('"shape": "square"', json.dumps(shapes), re.M):
    print("exists")
