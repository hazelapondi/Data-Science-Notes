import pandas as pd

brics = pd.read_csv("path/to/brics.csv", index_col = 0) #ensure to tell the 'read_csv' function that the first column contains row indexes with 'index_col' argument

brics.loc["BR"] #to access a row

brics.loc["CH","capital"] #for element access

#or brics["capital"].loc["CH"]  or brics.loc["CH"]["capital"]