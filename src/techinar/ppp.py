import pandas as pd
pizza_file='data/pizzas.csv'
pizza_data=pd.read_csv(pizza_file)
print(pizza_data)

import math
pizza_data['Area']=[((diameter/2)**2)*math.pi for diameter in pizza_data['Size']]
pizza_data['Price_per_SqInch']=[price/pizza_data['Area'] for price in pizza_data['Price']]
pizzas=pizza_data.sort_values(by)