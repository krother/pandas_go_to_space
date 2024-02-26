import pandas as pd
import numpy as np

np.random.seed(42)
N = 500
EARS = ['black', 'white', 'pink', 'blue', 'green', 'red', 'neon', 'orange', 'chartreuse', 'indigo', 'peachpuff', 'piercing', None]

index = pd.Series(np.arange(N), name='id')

df = pd.DataFrame(
    {
        'white_spots': np.random.randint(1, 20, size=N),
        'black_spots': np.random.randint(1, 20, size=N),
        'ears': np.random.choice(EARS, size=N)
    },
    index=index
)
df.to_csv('crew.csv')
