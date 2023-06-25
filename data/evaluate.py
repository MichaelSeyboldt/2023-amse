import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from geopy.geocoders import Nominatim


plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger

### vars deffs

us_ev_columns = ["ev_id", "ev_type", "ev_date", "ev_city", "ev_state", "ev_country", 
		"ev_year", "latitude", "longitude", "ev_highest_injury",
		"inj_tot_f", "inj_tot_m", "inj_tot_n",
		"inj_tot_s", "inj_tot_t", "dec_latitude", "dec_longitude"]
us_ac_columns = ["ev_id", "Aircraft_Key", "damage", "acft_make", "acft_model", "acft_series",
		"acft_category", "acft_reg_cls", "elt_manufacturer", "elt_model"]
us_ij_columns = ["ev_id", "Aircraft_Key", "inj_person_category", "injury_level", "inj_person_count"]


min_year = 2000 
max_year = 2023

##get datasets from databases in memory

genAvDE = pd.read_sql_table("generalAviation", "sqlite:///de.sqlite")
comAvDE = pd.read_sql_table("commercialAviation", "sqlite:///de.sqlite")
dataDE = pd.concat([genAvDE, comAvDE])

dataDE = dataDE.drop(columns="Kurzdarstellung")
print("DE data loaded")
print(dataDE.info())
print()
dataDE = dataDE.drop_duplicates()
dataDE.info()

dataDE.to_sql("all", "sqlite:///de.sqlite", if_exists="replace", index=False)

eventsUS = pd.read_sql_table("events", "sqlite:///us.sqlite")
aircraftUS = pd.read_sql_table("aircraft", "sqlite:///us.sqlite")
injuryUS = pd.read_sql_table("injury", "sqlite:///us.sqlite")

eventsUS = eventsUS[us_ev_columns]
eventsUS = eventsUS[eventsUS['ev_id'] != r',NONE"']
eventsUS = eventsUS[eventsUS['ev_id'] != r',FATL"']
aircraftUS = aircraftUS[us_ac_columns]
injuryUS = injuryUS[us_ij_columns]

# moved to convert
# usOnlyEvents = eventsUS[eventsUS["ev_country"]=="USA"]


def interpret_coord(coord, evid):
	print(len(coord.strip()))
	print(evid)
	if len(coord.strip()) == 0:
		return np.nan
	
	direction = coord[-1]
	sec = coord[-3:-1]
	if not sec.isnumeric():
		return np.nan
	minutes = coord[-5:-3]
	if not minutes.isnumeric():
		return np.nan
	deg = coord[:-5]
	if not deg.isnumeric():
		return np.nan
	dd = float(deg) + float(minutes)/60 + float(sec)/(60*60)
	if direction == 'W' or direction == 'S':
		dd *= -1
	return dd

def sum_3(a, b, c):
	if isinstance(a, int) or isinstance(a, str) and a.isnumeric():
		a = int(a)
	else:
		a = 0
	if isinstance(b, int) or isinstance(b, str) and b.isnumeric():
		b = int(b)
	else:
		b = 0
	if isinstance(c, int) or isinstance(c, str) and c.isnumeric():
		c = int(c)
	else:
		c = 0
	return a+b+c 
	


print(eventsUS.info())
# try to get missing decimal lat /  longitude from fields
eventsUS["dec_latitude"] = eventsUS.apply(lambda row: interpret_coord(row['latitude'], row['ev_id']) if row['dec_latitude'] is None or row['dec_latitude'] == "" else row['dec_latitude'], axis=1)
eventsUS["dec_longitude"] = eventsUS.apply(lambda row: interpret_coord(row['longitude'], row['ev_id']) if row['dec_longitude'] is None or row['dec_longitude'] == "" else row['dec_longitude'], axis=1)

print(eventsUS.info())
print(eventsUS.head(5))

eventsUS = eventsUS.fillna(value={"ev_highest_injury": "NONE", "inj_tot_f": 0, "inj_tot_m": 0, "inj_tot_n": 0,"inj_tot_s": 0, "inj_tot_t": 0})
# fix wrong total injury count where non injured persons where counted
eventsUS["inj_tot_t"] = eventsUS.apply(lambda row: sum_3(row['inj_tot_f'], row['inj_tot_m'], row['inj_tot_s']), axis=1 )
eventsUS.to_sql("events_clean", "sqlite:///us.sqlite", if_exists="replace", index=False)

#analyitics DE

jSplitFullDE = dataDE['Jahr'].value_counts(sort=False)
jSplitGADE = genAvDE['Jahr'].value_counts(sort=False)
jSplitCADE = comAvDE['Jahr'].value_counts(sort=False)

aufteilung = pd.merge(pd.merge(jSplitFullDE, jSplitGADE, how="left", on="Jahr"), jSplitCADE, how="left",on="Jahr")


aufteilung = aufteilung.rename({"count_x": "Sum", "count_y": "GeneralAviation","count": "CommericalAviation"}, axis=1)
aufteilung.to_sql("incidentAnalysisDE","sqlite:///results.sqlite", if_exists="replace", index=True) 


#analytics US

partUS = pd.merge(eventsUS, aircraftUS, how="left", on=["ev_id"], validate="1:m")
dataUS = pd.merge(partUS, injuryUS, how="left", on=["ev_id","Aircraft_Key"], validate="1:m")

aufteilungUS = eventsUS['ev_year'].value_counts(sort=False)
aufteilungUS = aufteilungUS.sort_index()

aufteilungUS.to_sql("incidentAnalysisUS", "sqlite:///results.sqlite", if_exists="replace", index=True)
