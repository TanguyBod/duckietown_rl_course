import pandas as pd

# Charger les fichiers Parquet
df1 = pd.read_parquet("./dataset/expert_data_14414.parquet")
df2 = pd.read_parquet("./dataset/expert_data_20361.parquet")

# Fusionner (concaténation verticale)
df_merged = pd.concat([df1, df2], ignore_index=True)

# Sauvegarder le résultat
df_merged.to_parquet("./dataset/data_fus.parquet")
