# 1. by a column
g1 = df.groupby('species')
g1.groups

# 2. by a boolean mask
mask = np.array(([False, True] * 300)[:df.shape[0]])
g2 = df.groupby(mask)
g2.groups

# 3. by a Dictionary with keys on the Index
groups = {1: "group A", 2: "group B", 
            3: "group C", 4: "group A", 
            ...}
g3 = df.groupby(groups)
g3.groups

# 4. by a function
g4 = df.groupby(len)
g4.groups

# 5. a list of the above
g5 = df.groupby(['species', mask, len])
g5.groups
