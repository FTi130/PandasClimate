import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv("https://raw.githubusercontent.com/shwars/PythonJump/master/Data/climat_russia_cities.csv")
data
data.columns=["City","Lat","Long","TempMin","TempColdest","AvgAnnual","TempWarmest","AbsMax","Precipitation"]
data["TempMin"] = pd.to_numeric(data["TempMin"])
data = data.apply(pd.to_numeric,errors='ignore')
for x in ["TempMin","TempColdest","AvgAnnual"]:
    data[x] = data[x].str.replace('−','-')

print(data.dtypes)




