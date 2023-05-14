import pandas as pd

commercialAircraft1 = pd.read_csv("ca_a1.csv", sep=';', encoding='iso-8859-1')
commercialAircraft1.to_sql("commercialAviation", 'sqlite:///de.sqlite', if_exists='replace', index=False)

commercialAircraft2 = pd.read_csv("ca_a2.csv", sep=';', encoding='iso-8859-1')

ca2 = commercialAircraft2.drop(columns = ['Unnamed: 12', 'Unnamed: 13'])
ca2.to_sql("commercialAviation", 'sqlite:///de.sqlite', if_exists='append', index=False)

generalAviation1 = pd.read_csv("ga_b1.csv", sep=';', encoding='iso-8859-1')
generalAviation1.to_sql("generalAviation", 'sqlite:///de.sqlite', if_exists='replace', index=False)

generalAviation2 = pd.read_csv("ga_b2.csv", sep=';', encoding='iso-8859-1')
generalAviation2.to_sql("generalAviation", 'sqlite:///de.sqlite', if_exists='append', index=False)


