import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger

##get datasets from databases in memory

genAvDE = pd.read_sql_table("generalAviation", "sqlite:///de.sqlite")
comAvDE = pd.read_sql_table("commercialAviation", "sqlite:///de.sqlite")
dataDE = pd.concat([genAvDE,comAvDE])

print("DE data loaded")
print(genAvDE.info())
print()
print(comAvDE.info())
print()
print(dataDE.info())
print()


eventsUS = pd.read_sql_table("events", "sqlite:///us.sqlite")
aircraftUS =  pd.read_sql_table("aircraft", "sqlite:///us.sqlite")
injuryUS =  pd.read_sql_table("injury", "sqlite:///us.sqlite")

usOnlyEvents = eventsUS[eventsUS["ev_country"]=="USA"]

partUS = pd.merge(usOnlyEvents, aircraftUS, how="left", on=["ev_id"], validate="1:m")
dataUS = pd.merge(partUS, injuryUS, how="left", on=["ev_id","Aircraft_Key"], validate="1:m")

print("US data loaded")
print(usOnlyEvents.info())
print()
print(dataUS.info())
