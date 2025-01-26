import seaborn as sns

df = sns.load_dataset("penguins")

# calculate the average body mass by species
df.groupby("species")["body_mass_g"].mean()

# calculate the average body mass by two criteria
df.groupby(["species", "sex"])["body_mass_g"].mean()

# save the per-species mean as a new column
df["mean_species_mass"] = df.groupby("species")["body_mass_g"].transform("mean")

# use multiple aggregation functions
df.groupby("species")["body_mass_g"].agg(["mean", "min", "max"])
