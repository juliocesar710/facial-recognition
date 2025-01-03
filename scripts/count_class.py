import pandas as pd

# Carregar o CSV de atributos
df = pd.read_csv('list_attr_celeba.csv')

# Contar as classes
male_count = len(df[df['Male'] == 1])
female_count = len(df[df['Male'] == -1])

print(f"Imagens com 'Male': {male_count}")
print(f"Imagens com 'Female': {female_count}")
