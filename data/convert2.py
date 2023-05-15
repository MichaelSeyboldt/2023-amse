from meza import io
import pandas as pd

tableNames = ["events", "aircraft","injury"]

for tableName in tableNames:
    dataFrame = pd.DataFrame(io.read("avall.mdb", table=tableName))
    dataFrame.to_sql(tableName, 'sqlite:///us.sqlite', if_exists='replace', index=False)


