import pandas as pd
import random

# Load the Excel file
try:
    file_path = 'input/foods.xlsx'
    df = pd.read_excel(file_path)

    # # Print the DataFrame
    # print(df)
    # print('')

    # # Sort the DataFrame by 'column_name' in descending order
    # sorted_df = df.sort_values(by='Rating', ascending=False)

    # # Print the sorted DataFrame
    # print(sorted_df)
except:
    print('EXCEPTION => File cannot be opened:', file_path)
    exit()

try:
    def create_calendar_menu(df):
        # Create a list for the calendar
        menu = []
        # Create a dictionary to hold the count of how many times each food item should appear
        food_count = {}
        #Days we want a meal per month
        days_per_month = 16

        # Determine the frequency of each food item based on its rating
        for index, row in df.iterrows():
            food_item = row['Food']
            rating = row['Rating']

            if rating >= 4:
                food_count[food_item] = 3
            elif rating >= 2:
                food_count[food_item] = 2
            else:
                food_count[food_item] = 1  # 1 time for rating 1

        # Flatten the food items according to the counts
        for food_item, count in food_count.items():
            for _ in range(count):
                menu.append(food_item)
        # print(food_count)

        # x = len(menu)
        # if x != 0:
        #     print('Items on menu: ' + str(x) + '\n' + str(menu))

        # Ensure the menu has 30 items for a month
        if len(menu) < 16:
            # Add random food items to reach 30 if needed
            while len(menu) < 16:
                menu.append(random.choice(df['Food'].tolist()))

        # Shuffle the menu to randomize the order
        random.shuffle(menu)
        # print(menu)

        for item in menu:
            if menu.count(item) > 1:
                menu.remove(item)
            while len(menu) < days_per_month:
                menu.append(random.choice(df['Food'].tolist()))

        #print(menu)

        # Create a calendar structure (6 weeks to accommodate 30 days)
        calendar = [['' for _ in range(7)] for _ in range(4)]
        day_counter = 1
        
        # Fill the calendar with food items only for Monday to Thursday
        for week in range(4):  # Up to 6 weeks
            used_items = set()  # Set to track used food items for the week
            for day in range(4):  # Only fill Monday to Thursday (0, 1, 2, 3)
                if day_counter > 30:
                    break
                # Attempt to find a unique food item for the current day
                food_item = None
                while food_item is None:
                    if menu:
                        candidate_item = menu.pop(0)  # Get the next item from the menu
                        if candidate_item not in used_items:  # Check for duplicates
                            food_item = candidate_item  # Assign the unique item
                            used_items.add(food_item)  # Add to the used items
                    else:
                        break  # Break if there are no more items in the menu
                
                calendar[week][day] = food_item if food_item else ''  # Assign item or leave empty
                day_counter += 1

        return calendar

    def print_calendar(calendar):
        print("Mo     Tu       We       Th       Fr    Sa    Su")  # Adjusted for spacing
        for week in calendar:
            # Join food items or empty strings with appropriate formatting
            week_display = ' | '.join(f"{item}" if item else "   " for item in week)
            print(week_display)

    # Generate and display the calendar menu
    calendar = create_calendar_menu(df)
    print_calendar(calendar)
       
except:
    print('EXCEPTION => Error occurred in create_calendar_menu()')
    exit()


