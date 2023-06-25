from meza import io
import pandas as pd

tableNames = ["events", "aircraft","injury"]

for tableName in tableNames:
    dataFrame = pd.DataFrame(io.read("avall.mdb", table=tableName))
    dataFrame = dataFrame[dataFrame['ev_id'].str.len()==14]
    if tableName =='events':
        dataFrame = dataFrame[dataFrame['ev_country']=="USA"]
    dataFrame.to_sql(tableName, 'sqlite:///us.sqlite', if_exists='replace', index=False)

    dataFrame2 = pd.DataFrame(io.read("Pre2008.mdb", table=tableName))
    dataFrame2 = dataFrame2[dataFrame2["ev_id"].str.len()==14]
    if tableName =='events':
        dataFrame2 = dataFrame2[dataFrame2['ev_country']=="USA"]
    dataFrame2.to_sql(tableName, 'sqlite:///us.sqlite', if_exists='append', index=False)

