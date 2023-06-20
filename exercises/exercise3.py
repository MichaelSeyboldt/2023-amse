import pandas as pd

# definitions
src = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
columns = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
column_names = ["date", "CIN", "name", "petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]
data_types = {"date": str, "CIN": str, "name": str, "petrol": int, "diesel": int,
              "gas": int, "electro": int, "hybrid": int, "plugInHybrid": int,
              "others": int}
data_types_no_names = {0: str, 1: str, 2: str, 12: int, 22: int,
              32: int, 42: int, 52: int, 62: int,
              72: int}
c_gt_zero = ["petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]

# extract
data = pd.read_csv(src, sep=";", encoding="latin_1", skiprows=7, skipfooter=2,
                   header=None, usecols=columns, engine="python", dtype=str,
                   na_values=["-", "nan", "NaN"], keep_default_na=True)
print(data.info())
print(data.head(5))

# shape
data.dropna(inplace=True)
data.columns = column_names
data = data.astype(dtype=data_types)
print(data.info())
print(data.head(5))

# validate
data = data[(data['CIN'].str.len()==5)]
for c_name in c_gt_zero:
    data = data[data[c_name]>0]

print(data.info())
print(data.head(5))

data.to_sql("cars", "sqlite:///cars.sqlite", if_exists="replace", index=False)

