''' This module provides functions for creating of project folders. '''

################################################
# Import necessary libraries

import time
# for use of sleep function

import gjrich_utils
# import module 1 library from gjrich_utils.py

from pathlib import Path
# importing for use of the Path object and the joinpath function


# Define Global Variables
# Create a top level path object at current directory
project_path = Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

# Set duration for sleep between folder creations; in unit of seconds
sleep_duration=3.0


# Function 1. Create a function to generate folders for a given range (e.g., years).
# Do this using for item in range
def create_folders_for_range(start_year: int, end_year: int):
    
    for year in range(start_year, end_year + 1):
    # note: the range function truncates 1 before the last value in the range, necessitating the + 1
        year=str(year)
        year_path=data_path.joinpath(year) 
        #appends the item's name to the data directory

        year_path.mkdir(exist_ok=True)
        print(f"Created folder for {year} at {year_path}")      
        time.sleep(sleep_duration) 


# Function 2. For Item in List: Develop a function to create folders from a list of names.
def create_folders_from_list(folder_list: list):
    
    for item in folder_list:
        
        has_spaces = " " in item
        has_uppercase = any(char.isupper() for char in item)
        
            
        if has_spaces:
            print(f"Removing spaces from name of {item}")
            item=item.replace(" ","")
        # Use conditional branching to remove spaces.
        
        if has_uppercase:
            print(f"Converting uppercase characters in {item} to lowercase characters")
            item=item.lower()
        # Use conditional branching to remove spaces.       
        
        item_path=data_path.joinpath(item)
        #appends the item's name to the data directory
        
        item_path.mkdir(exist_ok=True)
        print(f"Created folder for {item} at {item_path}")      
        time.sleep(sleep_duration)    
    
    
# Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
def create_prefixed_folders(folder_list: list, prefix: str):
    
    folder_list = [prefix + item for item in folder_list]
    # Use a list comprehension to demonstrate transforming a list into a new list.
    # this is done to add a prefix
    
    for item in folder_list:
        
        item_path=data_path.joinpath(item)
        item_path.mkdir(exist_ok=True)
        print(f"Created folder for {item} at {item_path}")      
        time.sleep(sleep_duration)
    
    
    

# Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
def create_folders_periodically(duration:int):

    start_tick=time.time()
        # check the time
    current_tick=start_tick
    tick_tock=0
        # initialize time measurement and guarantee it's larger than duration to initialize while variable
        
    incrementer=1

    while tick_tock<duration:
    
        folder_name="folder"+str(incrementer)
        item_path=data_path.joinpath(folder_name)
        item_path.mkdir(exist_ok=True)
        print(f"Created folder at {folder_name}")
        print("Next one in 5 seconds!")
        current_tick=time.time()
        tick_tock=current_tick-start_tick
                # Calculate the difference between start and current time

        
        time.sleep(5)
        
        incrementer=incrementer+1
            
            
            
            



def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {gjrich_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_list = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_list)

    # Call function 3 to create folders using comprehension
    folder_list = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_list, prefix)

    # Call function 4 to create folders periodically using while
    duration = 5  # duration in seconds
    create_folders_periodically(duration)


    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions)
    
    
    
if __name__ == '__main__':
    main()