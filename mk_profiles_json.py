# code: utf-8

####################################
# Make profiles file for Windows Terminal

import os
import json
import random
from pprint import pprint

# Read template json file
with open('template.json') as f:
    profiles = json.load(f)

# Set random wall paper
wall_paper_path = os.path.join(os.getenv('onedrive'), 'Pictures', '相机导入')
random_path = os.path.join(
    wall_paper_path, random.choice(os.listdir(wall_paper_path)))

# Available schemes
schemes = {e['name']: e for e in profiles['schemes']}
pprint(schemes)
random_schemes = random.choice([e for e in schemes])

# Choices
choices = dict(backgroundImage=random_path,
               colorSchemes=random_schemes,)
defaults = dict(backgroundImage=os.path.join(wall_paper_path, 'zeppelin.png'),
                colorSchemes='Zenburn',)
pprint(choices)

# Setup profiles parameters
select = choices
for j, e in enumerate(profiles['profiles']):
    e['backgroundImage'] = select['backgroundImage']
    e['backgroundImageOpacity'] = 0.5
    e['acrylicOpacity'] = 0.5
    # select['colorSchemes']  # random_schemes  # 'Night Owl'
    e['colorScheme'] = 'MaterialOcean'

# Write settings json file
# encoding='utf-8' and ensure_ascii is for Chinese characters.
with open('..\\LocalState\\settings.json', 'w', encoding='utf8') as f:
    json.dump(profiles, f, ensure_ascii=False)
