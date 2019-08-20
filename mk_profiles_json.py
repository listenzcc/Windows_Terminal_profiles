# code: utf-8

####################################
# Make profiles file for Windows Terminal

import os
import json
import random

# Read template json file
with open('template.json') as f:
    profiles = json.load(f)

# Set random wall paper
wall_paper_path = 'C:\\Users\\liste\\Pictures\\WallPapers'

for j in range(len(profiles['profiles'])):
    profiles['profiles'][j]['backgroundImage'] = os.path.join(
        wall_paper_path, random.choice(os.listdir(wall_paper_path)))
    profiles['profiles'][j]['backgroundImageOpacity'] = 0.2

# Unset startingDirectory
profiles['profiles'][0].pop('startingDirectory')

# Write profiles json file
with open('profiles.json', 'w') as f:
    json.dump(profiles, f)
