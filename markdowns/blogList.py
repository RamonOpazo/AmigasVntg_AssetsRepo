import yaml
import sys

f = '''---
title: Lorem ipsum dolor
author: Ramón Opazo
date: 16/08/2020
tags: test, blog, formatting
description: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus felis nisi, ultrices sed purus feugiat, placerat viverra ligula. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc luctus dui nisi, eget vehicula erat consequat in. Nunc in eleifend diam. Aliquam lacus mi, vestibulum sit amet ultricies in, mollis vel urna. Vestibulum odio tellus, dapibus ut diam vel, imperdiet fermentum tellus. Nunc lacinia bibendum tellus, non hendrerit ex euismod eu. Sed mattis lacus a lorem sollicitudin ornare. Phasellus urna tellus, condimentum non magna sed, tincidunt luctus orci. Aliquam at egestas diam. Donec auctor ultrices dignissim.
---'''

def get_yaml(f):
  pointer = f.tell()
  if f.readline() != '---\n':
    f.seek(pointer)
    return ''
  readline = iter(f.readline, '')
  readline = iter(readline.__next__, '---\n') #underscores needed for Python3?
  return ''.join(readline)

# Remove sys.argv, not sure what it was doing
#with open(filepath, encoding='UTF-8') as f:
config = list(yaml.load_all(get_yaml(f), Loader=yaml.SafeLoader)) # Load all to get all the YAML documents, Loader option required for most recent PyYAML, and list because it was originally returning a generator object
text = f.read()
print("TEXT from", f)
#print(text)
print("CONFIG from", f)
print(config)

