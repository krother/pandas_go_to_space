import requests
import re
import pandas as pd
import numpy as np

base_url = "https://en.everybodywiki.com/List_of_Star_Trek_planets"
char_ranges = ("AB", "CF", "GL", "MQ", "RS", "TZ")
pattern = r'<span id="[^"]+">([^>]+)</span>|<li><b>([^>]+)</b>|<p><b>([^<]+)</b>'

# scrape planet names
names = []
for char_from, char_to in char_ranges:
    url = f"{base_url}_({char_from}%E2%80%93{char_to})"
    page = requests.get(url)
    found_names = re.findall(pattern, page.text)
    print(char_from, char_to, len(found_names))
    names += [''.join(n) for n in found_names]


# create a table with planets
names = np.array(names)
np.random.seed(42)  # the answer to everything
np.random.shuffle(names)
n = len(names)

planets = pd.DataFrame({
    'name': names,
    'x': np.random.random(size=(n,)) * 100,
    'y': np.random.random(size=(n,)) * 100,
    'z': np.random.random(size=(n,)) * 100,
    'class': np.random.choice(np.array(list('MABC')), size=(n,)),
    'size': np.random.randint(1, 20, size=(n,)),
})

# write planets to files
planets.iloc[:300].to_csv('panda_sector.csv')
planets.iloc[300:600].to_csv('penguin_sector.csv')
planets.iloc[600:].to_csv('amoeba_sector.csv')
