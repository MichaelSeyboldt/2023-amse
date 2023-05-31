from meza import io
import pandas as pd

tableNames = ["events", "aircraft","injury"]

for tableName in tableNames:
    dataFrame = pd.DataFrame(io.read("avall.mdb", table=tableName))
    dataFrame.to_sql(tableName, 'sqlite:///us.sqlite', if_exists='replace', index=False)
    dataFrame2 = pd.DataFrame(io.read("Pre2008.mdb", table=tableName))
    dataFrame2.to_sql(tableName, 'sqlite:///us.sqlite', if_exists='append', index=False)

eventsFrame = pd.DataFrame(io.read("avall.mdb", table="events"))
aircraftFrame = pd.DataFrame(io.read("avall.mdb", table="aircraft"))
injuryFrame = pd.DataFrame(io.read("avall.mdb", table="injury"))
partFrame = pd.merge(eventsFrame, aircraftFrame, how="left", on="ev_id",validate="1:m" )
fullFrame = pd.merge(partFrame, injuryFrame, how="left", on=["ev_id","Aircraft_Key"])
fullFrame.to_sql("fullTable", 'sqlite:///us.sqlite', if_exists='replace', index=False)



