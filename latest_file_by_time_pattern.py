import os
import glob

def latest_file_by_time_pattern(pattern):
    latest_files = {}
    search_pattern = os.path.join(f'{pattern}*')
    files = glob.glob(search_pattern)
    print(files)

    if files:
        latest_file = max(files, key=os.path.getmtime)
        latest_files[pattern] = latest_file
    print(latest_files[pattern])    

latest_file_by_time_pattern("Breakdown_")    
latest_file_by_time_pattern("Country_BU_")    
