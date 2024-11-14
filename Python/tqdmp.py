from tqdm import tqdm

import time

import os

os.system('clear')

people_names = ['john', 'james', 'mary', 'damas']

[print(name) for name in tqdm(people_names, desc='People Names')]

for i in tqdm(range(10000), desc="Basic Loop"):
   
    time.sleep(0.001)