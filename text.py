import pandas as pd
import random

# Sample DataFrame
data = {
    'Food': ['Pizza', 'Burger', 'Salad', 'Chicken', 'Pasta', 'Steak', 'Lamb'],
    'Rating': [5, 4, 3, 4, 2, 1, 6]
}

df = pd.DataFrame(data)
days_per_week = 4

# Iterating over rows using iterrows()
for index, row in df.iterrows():
    print(f"Index: {index}, Food: {row['Food']}, Rating: {row['Rating']}")

menu = []

while len(menu) < days_per_week:
    menu.append(random.choice(df['Food'].tolist()))

random.shuffle(menu)
print(menu)
# print(len(set(menu)))
# print(set(menu))
# print(days_per_week)


for item in menu:
    if menu.count(item) > 1:
        menu.remove(item)
    while len(menu) < days_per_week:
        menu.append(random.choice(df['Food'].tolist()))

print(menu)