import os, subprocess
import pandas as pd, numpy as np

df_2009 = pd.read_parquet('data/yellow_tripdata_2009-01.parquet')

df_2015 = pd.read_parquet('data/green_tripdata_2015-01.parquet')


number = 50
desired_width = 5
number_str = "{:0>{}}".format(number, desired_width)
print("Number after leading zeros: ") 
print(number_str)

location = '/Users/phucnm/git/misc/NYC_Taxi_Data_Pipeline/data'

for year in range(2019,2023):
    for month in range(10,12):
        month_str = '{:0>{}}'.format(month, 2)
        try:
            subprocess.run(f'curl -o {location}/yellow_tripdata_{year}-{month_str}.parquet https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month_str}.parquet', shell=True)
        except:
            print('can not download')
        try:
            subprocess.run(f'curl -o {location}/green_tripdata_{year}-{month_str}.parquet https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month_str}.parquet', shell=True)
        except:
            print('can not download')
        try:
            subprocess.run(f'curl -o {location}/fhv_tripdata_{year}-{month_str}.parquet https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month_str}.parquet', shell=True)
        except:
            print('can not download')
        try:
            subprocess.run(f'curl -o {location}/fhvhv_tripdata_{year}-{month_str}.parquet https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month_str}.parquet', shell=True)
        except:
            print('can not download')
    
            

subprocess.run(f'curl -O {location} https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet', shell=False)
subprocess.run(f'cd {location}', shell=False)
