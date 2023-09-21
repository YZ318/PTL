import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
data_encoded = pd.get_dummies(data['whoAmI'])

# Объединяем исходный DataFrame с преобразованным one-hot столбцами
data_encoded = pd.concat([data, data_encoded], axis=1)
data_encoded = data_encoded.drop('whoAmI', axis=1)

data_encoded.head()
