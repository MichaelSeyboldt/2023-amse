import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

commercialAircraft1 = pd.read_csv("ca_a1.csv", sep=';', encoding='iso-8859-1')
locations = pd.DataFrame(commercialAircraft1["Unfallort"])

print(locations.info())

# commercialAircraft1["latitude", "longitude"] = commercialAircraft1.apply(lambda row : locate(row["Unfallort"]), axis=1)
commercialAircraft1.to_sql("commercialAviation", 'sqlite:///de.sqlite', if_exists='replace', index=False)

commercialAircraft2 = pd.read_csv("ca_a2.csv", sep=';', encoding='iso-8859-1')
ca2 = commercialAircraft2.drop(columns = ['Unnamed: 12', 'Unnamed: 13'])
# commercialAircraft2["latitude", "longitude"] = commercialAircraft2.apply(lambda row : locate(row["Unfallort"]), axis=1)
locations = pd.concat([locations, pd.DataFrame(ca2["Unfallort"])])

ca2.to_sql("commercialAviation", 'sqlite:///de.sqlite', if_exists='append', index=False)

generalAviation1 = pd.read_csv("ga_b1.csv", sep=';', encoding='iso-8859-1')
# generalAviation1["latitude", "longitude"] = generalAviation1.apply(lambda row : locate(row["Unfallort"]), axis=1)
locations = pd.concat([locations, pd.DataFrame(generalAviation1["Unfallort"])])
generalAviation1.to_sql("generalAviation", 'sqlite:///de.sqlite', if_exists='replace', index=False)

generalAviation2 = pd.read_csv("ga_b2.csv", sep=';', encoding='iso-8859-1')
# generalAviation2["latitude", "longitude"] = generalAviation2.apply(lambda row : locate(row["Unfallort"]), axis=1)
locations = pd.concat([locations, pd.DataFrame(generalAviation2["Unfallort"])])
generalAviation2.to_sql("generalAviation", 'sqlite:///de.sqlite', if_exists='append', index=False)

print(locations.info())
locations = locations.assign(latitude=np.nan, longitude=np.nan)
locations = locations.drop_duplicates()
locations = locations.astype( dtype={"Unfallort": str,"latitude": float,"longitude": float})
print(locations.info())
try:
    locations.to_sql("locations", "sqlite:///loc.de.sqlite", index=False, if_exists="fail")

except ValueError:
    print("database already exists")