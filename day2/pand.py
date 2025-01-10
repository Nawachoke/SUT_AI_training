import pandas as pd

data = {
    'Square_Footage':[1500, 1800, 2200, 1200, 2500],
    'Bedrooms':[3,4,5,2,3],
    'Bathrooms':[2,2.5,3,1.5,3],
    'Location':['Suburb', 'City Center', 'Suburb', 'Rural', 'City center'],
    'House_Price':[250000, 320000, 450000, 180000, 500000]
}

df = pd.DataFrame(data)

df.to_csv('day2/house_features.csv', index=False)

df2 = pd.read_csv('day2/house_features.csv')
print(df2)