import pandas as pd
from urllib.request import urlretrieve
import zipfile

src = 'https://gtfs.rhoenenergie-bus.de/GTFS.zip'
cols = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
dtypes= {"stop_id": int, "stop_name": str, "stop_lat": float, "stop_lon": float, "zone_id": int}


#load
fname , headers  = urlretrieve(src)
if fname is None or fname == -1:
    print(f"failed to open {src}. Aborting.\nHeaders: {headers}\n")
    exit(1)
with zipfile.ZipFile(fname, "r") as zip_ref:
    zip_ref.extract("stops.txt")

df = pd.read_csv("stops.txt", sep=',', usecols=cols, dtype=dtypes)

if df is None:
    print("failed to load data to pandas data frame")
    exit(1)

#validate
df = df[df['zone_id'] == 2001]
df = df[df['stop_lat'] >= -90]
df = df[df["stop_lat"] <= 90]
df = df[df['stop_lon'] >= -90]
df = df[df['stop_lon'] <= 90]
df = df.dropna()


#save
df.to_sql("stops", "sqlite:///gtfs.sqlite", if_exists="replace", index=False)
