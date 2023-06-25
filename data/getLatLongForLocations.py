import pandas as pd
import numpy as np
import time
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="asbhngaurfwe:3")

locator = geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def locate(ort):
    try:
        l = locator(ort)
    except:
        print("some error occured")
        return [ort, np.nan, np.nan]
    if l is None:
        print(f"could not get location for {ort}")
        return [ort, np.nan, np.nan]
    else:
        return [ort, l.latitude, l.longitude]


df = pd.read_sql("locations", "sqlite:///loc.de.sqlite")

df.info()
df.head()

df2 = df.apply(lambda row : locate(row["Unfallort"]), axis=1, result_type='expand')
df2.info()
df2.to_sql("locations-new", "sqlite:///loc.de.sqlite", if_exists="replace", index=False)
