import myfitnesspal
import datetime
import numpy as np
import pandas as pd

# Before you use this program for the first time. You need to store your myfitnesspal password
# Put this command into terminal to store password - 
# myfitnesspal store-password my_username)

print('Welcome to WeightCompare. Account for normal fluctuations by taking moving averages. Please enter username to begin.')
username = input('Username: ')
print('Please wait up to 30 seconds while data is retreived')
client = myfitnesspal.Client(username)

start_date = datetime.date(2000, 1, 1)
weight = client.get_measurements('Weight', start_date)
print('Data Retrieved')

# data is returned in an OrderedDict, I'm changing that into lists and creating a dataframe
date_keys = list(weight.keys())
weight_values = list(weight.values())
df = pd.DataFrame({"Date": date_keys, "Weight": weight_values})
df['Date'] = pd.to_datetime(df['Date'])

run = True
while run:
    today = datetime.date.today()
    period_length = input('Period Length (days): ')
    comparison_period = input('Comparison Period (days): ')
    delta1 = int(period_length)
    delta2 = int(comparison_period)
    length_delta = datetime.timedelta(days=delta1)
    comparison_delta = datetime.timedelta(days=delta2)
    current_range_start = (today-length_delta)
    current_range_end = (today)
    comparison_range_start = (today-comparison_delta-length_delta)
    comparison_range_end = (today-comparison_delta)
    
    current_df = df[(df['Date'] >= current_range_start) & (df['Date'] <= current_range_end)]
    current_weight_count = current_df[['Weight']].count().values[0]
    current_weight_avg = current_df[['Weight']].mean()
    current_weight_avg = str(round(current_weight_avg.values[0], 2))
    print('Over the last ' + period_length + ' days, you took ' + str(current_weight_count) + ' measurements, and your average weight is ' + current_weight_avg)
    
    comparison_df = df[(df['Date'] >= comparison_range_start) & (df['Date'] <= comparison_range_end)]
    comparison_weight_count = comparison_df[['Weight']].count().values[0]
    comparison_weight_avg = comparison_df[['Weight']].mean()
    comparison_weight_avg = str(round(comparison_weight_avg.values[0], 2))
    print('For the same period ' + comparison_period + ' days ago, you took ' + str(comparison_weight_count) + ' measurements, and your average weight was ' + comparison_weight_avg)
    
    run_again = input('Another query? y/n: ')
    if run_again in ['y', 'Y', 'yes', 'Yes', 'YES']:
        run = True
    else:
        print('Goodbye')
        run = False