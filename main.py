from dataclasses import dataclass

import pandas as pd
from pandas.conftest import fixed_now_ts, dtype_backend
from pyexpat.errors import messages

message_type = "Onsert"
start_date = "2024/11/10"
end_date = "2024/11/20"
message = "Onsert message"

directory = "C:"
df = pd.read_csv(directory+"Onsert.csv", converters={'Company' : str})
df ["ID"] = ""
df ["Document Type"] = ""
df ["Start Date"] = start_date
df ["End Date"] = end_date

if message_type == "Onsert":
    df["Message"] = message
    df = df[['ID', 'Company', 'Customer', 'Document Type', 'Document', 'Start Date', 'End Date', 'Message']]
elif message_type == "Insert":
    df = df[['ID', 'Company', 'Customer', 'Document Type', 'Document', 'Start Date', 'End Date']]

print(df)
df.to_csv("OnsertTemplate.csv", index=False)
