import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv("./nato_phonetic_alphabet.csv")
df_list = df.values.tolist()


df_dict = {x[0]: x[1] for x in df_list}
# print(df_dict)

name = input("Enter a name: ").upper()

name_list = [df_dict[letter] for letter in name]
print(name_list)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
