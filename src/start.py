import pandas as pd

from src.constants import AirlineDatabaseConstants

# after testing replace StringIO(temp) to filename

df = pd.read_csv("../resources/airlines.dat.txt")
df.columns = [AirlineDatabaseConstants.AIRLINE_ID,
              AirlineDatabaseConstants.NAME,
              AirlineDatabaseConstants.ALIAS,
              AirlineDatabaseConstants.IATA,
              AirlineDatabaseConstants.ICAO,
              AirlineDatabaseConstants.CALLSIGN,
              AirlineDatabaseConstants.COUNTRY,
              AirlineDatabaseConstants.ACTIVE]
print(df.iloc[1:10, :])
