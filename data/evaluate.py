import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger

### vars deffs

us_ev_columns = ["ev_id", "ev_type", "ev_date", "ev_city", "ev_state", "ev_country", 
		"ev_year", "ev_month", "latitude", "longitude", "apt_name", "ev_highest_injury",
		"inj_f_grnd", "inj_m_grnd", "inj_s_grnd", "inj_tot_f", "inj_tot_m", "inj_tot_n",
		"inj_tot_s", "inj_tot_t" ]
us_ac_columns = ["ev_id", "Aircraft_Key", "damage", "acft_make", "acft_model", "acft_series",
		"acft_category", "acft_reg_cls", "elt_manufacturer", "elt_model"]
us_ij_columns = ["ev_id", "Aircraft_Key", "inj_person_category", "injury_level", "inj_person_count"]


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

eventsUS = eventsUS[us_ev_columns]
aircraftUS = aircraftUS[us_ac_columns]
injuryUS = injuryUS[us_ij_columns]

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

aufteilungUS.to_sql("incidentAnalysisUS", "sqlite:///results.sqlite", if_exists="replace", index=False)
