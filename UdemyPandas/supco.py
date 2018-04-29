import pandas as pd
supco2 = pd.read_csv('supco2.csv', index_col = 'No')
supco2 = supco2.pivot(index='row',columns='col',values='value')
supco2.to_csv('supco2-converted.csv')
