import pandas as pd
from food import df  # Import the DataFrame from food.py
import random

# try:
#     def create_calendar_menu(df):
#         # Create a list for the calendar
#         menu = []

#         # Determine the frequency of each food item based on its rating
#         for index, row in df.iterrows():
#             food_item = row['Food']
#             rating = row['Rating']
            
#             if rating >= 4:
#                 menu.extend([food_item] * random.randint(2, 3))  # 2-3 times for ratings 4 and 5
#             elif rating >= 2:
#                 menu.extend([food_item] * random.randint(1, 2))  # 1-2 times for ratings 2 and 3
#             else:
#                 menu.append(food_item)  # 1 time for rating 1

#         # Ensure the menu has 30 items for a month
#         while len(menu) < 30:
#             menu.append(random.choice(df['Food'].tolist()))
#         print(menu)
#         # Shuffle the menu to randomize the order
#         random.shuffle(menu)

#         # Create a DataFrame for the calendar menu
#         calendar_menu = pd.DataFrame({'Day': range(1, 31), 'Food Item': menu})
#         print(calendar_menu)
#         return calendar_menu

#     # Generate and display the calendar menu
#     calendar_menu = create_calendar_menu(df)
#     print(calendar_menu.to_string(index=False))
# except:
#     print('EXCEPTION => Error occurred in create_calendar_menu()')
#     exit()

#try:
def create_calendar_menu(df):
    # Create a list for the calendar
    menu = []
    # Create a list of weeks (assuming 5 weeks for 30 days)
    weeks = [[] for _ in range(5)]
    # Create a dictionary to hold the count of how many times each food item should appear
    food_count = {}

    # Determine the frequency of each food item based on its rating
    for index, row in df.iterrows():
        food_item = row['Food']
        rating = row['Rating']

        if rating >= 4:
            food_count[food_item] = random.randint(2, 3)  # 2-3 times for ratings 4 and 5
        elif rating >= 2:
            food_count[food_item] = random.randint(1, 2)  # 1-2 times for ratings 2 and 3
        else:
            food_count[food_item] = 1  # 1 time for rating 1

    # Flatten the food items according to the counts
    for food_item, count in food_count.items():
        for _ in range(count):
            menu.append(food_item)

    # Ensure the menu has 30 items for a month
    if len(menu) < 30:
        # Add random food items to reach 30 if needed
        while len(menu) < 30:
            menu.append(random.choice(df['Food'].tolist()))
        
    # Shuffle the menu to randomize the order
    random.shuffle(menu)

    # Distribute food items across weeks without duplicates
    calendar_menu = pd.DataFrame(columns=['Day', 'Food Item'])
    day_counter = 1
    
    for week in weeks:
        for day in range(7):  # 7 days in a week
            if day_counter <= len(menu):
                food_item = menu[day_counter - 1]

                # Check if the food item is already in the current week
                if food_item not in week:
                    week.append(food_item)
                    # Create a new DataFrame for the current item
                    new_row = pd.DataFrame({'Day': [day_counter], 'Food Item': [food_item]})
                    # Concatenate the new row to the calendar_menu DataFrame
                    calendar_menu = pd.concat([calendar_menu, new_row], ignore_index=True)
                    day_counter += 1
    
    # Fill any remaining days with random food items if necessary
    while day_counter <= 30:
        random_food = random.choice(df['Food'].tolist())
        new_row = pd.DataFrame({'Day': [day_counter], 'Food Item': [random_food]})
        calendar_menu = pd.concat([calendar_menu, new_row], ignore_index=True)
        day_counter += 1

    return calendar_menu

# Generate and display the calendar menu
calendar_menu = create_calendar_menu(df)
print(calendar_menu.to_string(index=False))
# except:
    # print('EXCEPTION => Error occurred in create_calendar_menu()')
    # exit()

# try:
#     # Create a new DataFrame for the calendar layout
#     def create_calendar_layout(df):
#         # Create a DataFrame for the calendar
#         days_in_month = 30
#         weeks = (days_in_month + 6) // 7  # Calculate number of weeks needed
#         calendar_layout = pd.DataFrame(index=range(weeks), columns=range(7))

#         # Fill the calendar layout
#         for i in range(days_in_month):
#             week = i // 7
#             day_of_week = i % 7
#             calendar_layout.iloc[week, day_of_week] = df.iloc[i]['Food Item']

#         return calendar_layout

#     # Create the calendar layout
#     calendar_layout = create_calendar_layout(calendar_menu)

#     # Display the calendar layout
#     print(calendar_layout)
# except:
#     print('EXCEPTION => Error occurred in create_calendar_layout()')
#     exit()