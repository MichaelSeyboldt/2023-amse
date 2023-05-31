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

#analyitics DE

jSplitFullDE = dataDE['Jahr'].value_counts(sort=False)
jSplitGADE = genAvDE['Jahr'].value_counts(sort=False)
jSplitCADE = comAvDE['Jahr'].value_counts(sort=False)

aufteilung = pd.merge(pd.merge(jSplitFullDE, jSplitGADE, how="left", on="Jahr"), jSplitCADE, how="left",on="Jahr")

print()
print(f"we have data for {dataDE['Jahr'].nunique()} years")
print(f"with {dataDE['Aktenzeichen'].nunique()} incidents")
print(f"distributed by year {dataDE['Jahr'].value_counts(sort=False)}")
print("split by com and general aviation")
print(aufteilung)

aufteilung = aufteilung.rename({"count_x": "Sum", "count_y": "GeneralAviation","count": "CommericalAviation"}, axis=1)
print(f"and renamed \n{aufteilung}")
aufteilung.to_sql("incidentAnalysisDE","sqlite:///results.sqlite", if_exists="replace", index=False) 


#analytics US
print(f"we have data for {dataUS['ev_year'].nunique()} years")
print(f"with {dataUS['ev_id'].nunique()} incidents")
print(f"distributed by year \n{dataUS['ev_year'].value_counts(sort=False)}")
aufteilungUS = dataUS['ev_year'].value_counts(sort=False)
aufteilungUS = aufteilungUS.sort_index()
print(f"sorted: \n{aufteilungUS}")
