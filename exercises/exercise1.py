import pandas as pd

src = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
collumNames = ["ID", "name", "city", "country", "IATA_code", "ICAO_code", "latitude", "longitude",
               "elevation", "delta_time", "continent", "timezone", "geo_punkt"]
dataTypes = { "ID": int, "name": str, "city": str, "country": str, "IATA_code": str, "ICAO_code": str,
             "latitude": float, "longitude": float, "elevation": int, "delta_time": float, "continent": str,
             "timezone": str, "geo_punkt": str}

data = pd.read_csv(src, sep=';', header=0,names=collumNames,dtype=dataTypes)
print("data format:")
print(data.dtypes)
res = data.to_sql("airports", "sqlite:///airports.sqlite", if_exists="replace", index=False)
print(f"saved {res} rows of data")
