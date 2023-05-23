import pandas as pd

src = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
columnNames = ["ID", "name", "city", "country", "IATA_code", "ICAO_code", "latitude", "longitude",
               "elevation", "delta_time", "continent", "timezone", "geo_punkt"]
dataTypes = {"ID": int, "name": str, "city": str, "country": str, "IATA_code": str, "ICAO_code": str,
             "latitude": float, "longitude": float, "elevation": int, "delta_time": float, "continent": str,
             "timezone": str, "geo_punkt": str}
dtypeNoNames = {"column_1": int, "column_2": str, "column_3": str, "column_4": str, "column_5": str, "column_6": str,
                "column_7": float, "column_8": float, "column_9": int, "column_10": float, "column_11": str,
                "column_12": str, "geo_punkt": str}

data = pd.read_csv(src, sep=';', header=0,
                   #names=columnNames,dtype=dataTypes
                   dtype=dtypeNoNames)

print("data format:")
print(data.dtypes)
res = data.to_sql("airports", "sqlite:///airports.sqlite", if_exists="replace", index=False)
print(f"saved {res} rows of data")
